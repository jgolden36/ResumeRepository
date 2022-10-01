function NewtonsMethodQ1A(Guessx,Guessy)
SSE=(10-Guessx^2-Guessy^2)^2+(-10-Guessx+3*Guessy)^2;
while SSE>.000001
    Guessx=Guessx-(1/((12*Guessx^2-40+4*Guessy^2)-2))*(-4*(10-Guessx^2-Guessy^2)*Guessx+2*(-10-Guessx+3*Guessy));
    Guessy=Guessy-(1/((-40+4*Guessx^2+12*Guessy^2)+18))*(-4*(10-Guessx^2-Guessy^2)*Guessy+6*(-10-Guessx+3*Guessy));
    SSE=(10-Guessx^2-Guessy^2)^2+(-10-Guessx+3*Guessy)^2;
end
NewtonsMethodSolution = ['In the solution, x is valued at ', num2str(Guessx), ' and y is valued at', num2str(Guessy), '.']
end