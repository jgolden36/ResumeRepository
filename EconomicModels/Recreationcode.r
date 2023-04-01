library(psidR)
library(data.table)
library(tidyverse)
library(plm)
library(dplyr)
r<- system.file(package="psidR")
f<- fread(file.path("famvars1.csv"))
#i<-dcast(i[,list(year,name,variable)],year~name, value.var = "variable")
#f<-dcast(f[,list(year,name,variable)],year~name, value.var = "variable")
#SZz4FPKGvQPe5GR
d<-build.panel(datadir="C:/Users/bnhas/OneDrive/Desktop/Classes/Classes Spring 2023/Macro 4/Homework/Recreation/Data/data",fam.vars=f,heads.only = TRUE,design="all")
save(d,file="~/psid.Rda")
load("~/psid.Rda")
d<-d %>% drop_na()
d<-d %>%filter(Income>=0)
#d<-d %>%filter(Income!=9999999)
d<-d %>%filter(Income!=99999999)
#d<-d %>%filter(Income>=5000)
d$HourlyRate<-(d$Income/(d$Hours_Worked*52))
d$cohort<-d$year-d$Age
d$cohort<-as.factor(d$cohort)
d<-d %>%filter(Education!=99)
d<-d %>%filter(Age!=99)
d<-d %>%filter(Hours_Worked!=99)
d<-d %>%filter(Age>=22 & Age<=64&Hours_Worked>13&Hours_Worked<127)
#
#d<-d %>%filter(HourlyRate<=10000)
#&HourlyRate>=2&HourlyRate<=400&
d$LogIncome<-log(d$Income+1)
d<-setDT(d)[order(LogIncome)][,.SD[1,], by = .(pid, Age)] 
PData <- pdata.frame(d, index = c("pid", "Age"))
Model1<-plm(LogIncome~Age+cohort+Education+Hours_Worked,data=PData)
summary(Model1)
ModelResiduals<-Model1$residuals
Residualdf <- cbind(as.vector(ModelResiduals), attr(ModelResiduals, "index"))
names(Residualdf) <- c("resid", "pid", "Age")
#Residualdf%>%filter(Age!=25)
VarbyAge=aggregate(Residualdf$resid, list(Residualdf$Age), FUN=var)
VarbyAge
plot(VarbyAge)
MeanResbyAgeCurrent<-aggregate(Residualdf$resid, list(Residualdf$Age), FUN=mean)
Residualdf$Age<-as.numeric(Residualdf$Age)
ResTomorrow<-Residualdf %>%filter(Age!=1)
MeanResbyAgeTomorrow=aggregate(ResTomorrow$resid, list(ResTomorrow$Age), FUN=mean)
MeanResbyAgeCurrent$Age=MeanResbyAgeCurrent$Group.1
MeanResbyAgeCurrent$Age<-as.numeric(MeanResbyAgeCurrent$Age)
MeanResbyAgeTomorrow$Age=MeanResbyAgeTomorrow$Group.1-1
Residualdf$Age<-as.numeric(Residualdf$Age)
MeanMinusToday<-left_join(Residualdf,MeanResbyAgeCurrent, by='Age')
MeanMinusToday$difference<-MeanMinusToday$resid-MeanMinusToday$x
MeanMinusTomorrow<-inner_join(Residualdf,MeanResbyAgeTomorrow, by='Age')
MeanMinusTomorrow$difference1<-MeanMinusTomorrow$resid-MeanMinusTomorrow$x
MeanSubtractDataFrame<-inner_join(MeanMinusTomorrow,MeanMinusToday, by=c('Age','pid'))
MeanSubtractDataFrame$ProductCovar<-MeanSubtractDataFrame$difference*MeanSubtractDataFrame$difference1
CovarbyAge<-aggregate(MeanSubtractDataFrame$ProductCovar, list(MeanSubtractDataFrame$Age), FUN=sum)
TotalPeoplebyAge<-MeanSubtractDataFrame %>% count(Age)
CovarbyAge$Age<-CovarbyAge$Group.1
CovarbyAge<-inner_join(CovarbyAge,TotalPeoplebyAge, by=c('Age'))
CovarbyAge$x<-CovarbyAge$x/CovarbyAge$n
CovarbyAge<-CovarbyAge %>%filter(Age!=42)
plot(CovarbyAge$x)
CovarbyAge = subset(CovarbyAge, select = -c(Age,n) )
AugmentedDf<-rbind(CovarbyAge, VarbyAge)
MaximizationPotential <- function(k,VarianceMatrix) {
  rho<-k[1]
  sigmaAlpha<-k[2]
  sigmaEta<-k[3]
  sigmaEpsilon<-k[4]
  SumMatrix <- rep(0, 85)
  rhoTotal1=0
  for (i in 1:42) {
    SumMatrix[i]<-(VarianceMatrix$x[i]-sigmaAlpha-rho*(sigmaEta+rhoTotal1))
    rhoTotal1<-rhoTotal1+sigmaEta*rho^(2*i)
  }
  rhoTotal2<-0
  for (j in 43:84) {
    SumMatrix[j]<-(VarianceMatrix$x[j]-sigmaAlpha-sigmaEpsilon-sigmaEta-rhoTotal2)
    rhoTotal2<-rhoTotal2+sigmaEta*rho^(2*(j-42))
  }
  TotalSum=SumMatrix%*%diag(85)%*%SumMatrix
  #TotalSum=SumMatrix*SumMatrix
  return (sum(TotalSum))
}
optim(c(1,1,1,1), fn=MaximizationPotential,VarianceMatrix=AugmentedDf)
#c(x[1]+)
#flb <- function(x){ p <- length(x); sum((AugmentedDf-c()) *diag(80)*(AugmentedDf-)}
#res <- optim(rep(3, 25), flb, NULL, method = "L-BFGS-B", lower = rep(0,4))

