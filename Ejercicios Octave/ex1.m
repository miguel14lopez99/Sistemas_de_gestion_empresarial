clc
clear
M = [ 1 2 3 4 ; 5 6 7 8 ; 9 10 11 12 ; 13 14 15 16 ];

for i=1:1:size(M,1)
    
    if rem(i,2) != 0
        
        for j=1:1:size(M,2) 
            
            fprintf("%i ", M(i,j));
            
        end
        
    else
        
        for j=size(M,2):-1:1
            
            fprintf("%i ", M(i,j));
            
        end
        
    end
    fprintf("\n")
    
end
