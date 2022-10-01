function GradientDescentQ1D(Guessx,Guessy,alpha)
SSE=(26-Guessx^2-Guessy^2)^2+(100-3*Guessx^2-25*Guessy^2)^2;
while SSE>.001
    Guessx=Guessx-alpha*(-4*(26-Guessx^2-Guessy^2)*Guessx-12*Guessx*(100-3*Guessx^2-25*Guessy^2));
    Guessy=Guessy-alpha*(-4*(26-Guessx^2-Guessy^2)*Guessy-100*Guessy*(100-3*Guessx^2-25*Guessy^2));
    SSE=(26-Guessx^2-Guessy^2)^2+(100-3*Guessx^2-25*Guessy^2)^2;
end
GradientDescentSolution = ['In the solution, x is valued at ', num2str(Guessx), ' and y is valued at', num2str(Guessy), '.']
end