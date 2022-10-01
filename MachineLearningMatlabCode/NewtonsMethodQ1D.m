function NewtonsMethodQ1D(Guessx,Guessy)
SSE=(26-Guessx^2-Guessy^2)^2+(100-3*Guessx^2-25*Guessy^2)^2;
while SSE>.0001
    Guessx=Guessx-(1/((-4*(26-3*Guessx^2-Guessy^2))-12*(100-9*Guessx^2-25*Guessy^2)))*(-4*(26-Guessx^2-Guessy^2)*Guessx-12*Guessx*(100-3*Guessx^2-25*Guessy^2));
    Guessy=Guessy-(1/((-4*(26-Guessx^2-3*Guessy^2))-100*(100-3*Guessx^2-75*Guessy^2)))*(-4*(26-Guessx^2-Guessy^2)*Guessy-100*Guessy*(100-3*Guessx^2-25*Guessy^2));
    SSE=(26-Guessx^2-Guessy^2)^2+(100-3*Guessx^2-25*Guessy^2)^2;
end
GradientDescentSolution = ['In the solution, x is valued at ', num2str(Guessx), ' and y is valued at', num2str(Guessy), '.']
end