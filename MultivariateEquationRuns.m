function F = steadyStateSolver(k)
alpha=.3;
EfficiencyGrowth=.019;
populationGrowth=.012;
A=2;
beta=.97;
delta=.045;
sigma=3;
k0=(((1+EfficiencyGrowth)*(1+populationGrowth)+(-beta)*(1-delta))/(beta*alpha))^(1/(alpha-1))*.5;
F(1) = beta*(k(1)^alpha-k(2)*(1+EfficiencyGrowth)*(1+populationGrowth)+(1-delta)*k(1))^(-sigma)*(alpha*(k(1)^(alpha-1)))+beta*(1-delta)*(k(1)^alpha-k(2)*(1+populationGrowth)*(1+EfficiencyGrowth)+(1+delta)*k(1))^(-sigma)-((k0^alpha-k(1)*(1+EfficiencyGrowth)*(1+populationGrowth)+(1+delta)*k0)^(-sigma))*(1+EfficiencyGrowth)*(1+populationGrowth);
for i=1:498
	F(i+1) = beta*(k(i+1)^alpha-k(i+2)*(1+EfficiencyGrowth)*(1+populationGrowth)+(1-delta)*k(i+1))^(-sigma)*(alpha*(k(i+1)^(alpha-1)))+beta*(1-delta)*(k(i+1)^alpha-k(i+2)*(1+populationGrowth)*(1+EfficiencyGrowth)+(1+delta)*k(i+1))^(-sigma)-((k(i)^alpha-k(i+1)*(1+EfficiencyGrowth)*(1+populationGrowth)+(1+delta)*k(i))^(-sigma))*(1+EfficiencyGrowth)*(1+populationGrowth);
end
