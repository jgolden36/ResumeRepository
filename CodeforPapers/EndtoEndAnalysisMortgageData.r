library(readr)
library(rpart.plot)
library(ggplot2)
library(randomForest)
library(dplyr)
library(naivebayes)
library(class)
library(e1071)
library(rpart)
hmda_2017_ga_all_records_codes <-
  read_csv("C:/Users/bnhas/Downloads/hmda_2017_ga_all-records_codes
(3)/hmda_2017_ga_all-records_codes.csv")
mortgageMinor<-subset(hmda_2017_ga_all_records_codes,action_taken<=4)
mortgageMinor$action_taken <- ifelse(mortgageMinor$action_taken <= 2, 1, 0)
mortgageMinor$BlackRaceApp1<-ifelse(mortgageMinor$applicant_race_1 == 3, 1,
                                    0)
mortgageMinor$AsianRaceApp1<-ifelse(mortgageMinor$applicant_race_1 == 2, 1,
                                    0)
mortgageMinor$AmericanIndianRaceApp1<-ifelse(mortgageMinor$applicant_race_1
                                             == 1, 1, 0)
mortgageMinor$PacificIslander<-ifelse(mortgageMinor$applicant_race_1 == 4, 1,
                                      0)
mortgageMinor$White<-ifelse(mortgageMinor$applicant_race_1 == 5, 1, 0)
mortgageMinor$HispanicApplicant<-ifelse(mortgageMinor$applicant_ethnicity ==
                                          1, 1, 0)
mortgageMinor$HispanicCoApplicant<-
  ifelse(mortgageMinor$co_applicant_ethnicity == 1, 1, 0)
mortgageMinor$NonHispaniApplicant<-ifelse(mortgageMinor$applicant_ethnicity
                                          == 2, 1, 0)
mortgageMinor$NonHispanicCoApplicant<-
  ifelse(mortgageMinor$co_applicant_ethnicity == 2, 1, 0)
mortgageMinor$Male<-ifelse(mortgageMinor$applicant_sex == 1, 1, 0)
mortgageMinor$Female<-ifelse(mortgageMinor$applicant_sex == 2, 1, 0)
mortgageMinor$Owner_occupied<-ifelse(mortgageMinor$owner_occupancy == 1, 1,
                                     0)
mortgageMinor$HomeImprovement<-ifelse(mortgageMinor$loan_purpose == 2, 1, 0)
mortgageMinor$HomePurchase<-ifelse(mortgageMinor$loan_purpose == 1, 1, 0)
mortgageMinor$VAloan<-ifelse(mortgageMinor$loan_type == 3, 1, 0)
mortgageMinor$FHAloan<-ifelse(mortgageMinor$loan_type == 2, 1, 0)
mortgageMinor$FSAloan<-ifelse(mortgageMinor$loan_type == 4, 1, 0)
mortgageMinor$ManufacturedBuilding<-ifelse(mortgageMinor$property_type == 2,
                                           1, 0)
mortgageMinor$Multifamily<-ifelse(mortgageMinor$property_type == 3, 1, 0)
mortgageMinor$LoanPercentageofIncome<-
  (mortgageMinor$loan_amount_000s/mortgageMinor$applicant_income_000s)
mortgageMinor<-mortgageMinor[!is.na(mortgageMinor$BlackRaceApp1),]
mortgageMinor<-mortgageMinor[!is.na(mortgageMinor$AsianRaceApp1),]
mortgageMinor<-mortgageMinor[!is.na(mortgageMinor$AmericanIndianRaceApp1),]
