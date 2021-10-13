clc
clear

n = 100;

for i=1:1:n

    for j=1:1:n
        
        for k=1:1:n
            
            a = i^2 + j^2;
            b = k^2;
            
            if ( a == b && i+j+k == 30 )
                
                fprintf("%i^2 + %i^2 = %i^2\n", i, j, k );
                
            end
               
        end
        
    end

end


