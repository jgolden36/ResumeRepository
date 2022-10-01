function GradientDescentQ1A(Guessx,Guessy,alpha)
SSE=(10-Guessx^2-Guessy^2)^2+(-10-Guessx^2+3*Guessy)^2;
while SSE>.00001
    Guessx=Guessx-alpha*(-4*(10-Guessx^2-Guessy^2)*Guessx-2*(-10-Guessx+3*Guessy));
    Guessy=Guessy-alpha*(-4*(10-Guessx^2-Guessy^2)*Guessy+6*(-10-Guessx+3*Guessy));
    SSE=(10-Guessx^2-Guessy^2)^2+(-10-Guessx+3*Guessy)^2;
end
GradientDescentSolution = ['In the solution, x is valued at ', num2str(Guessx), ' and y is valued at', num2str(Guessy), '.']
end