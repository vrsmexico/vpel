#ES UNA VARIABLES GLOBAL





def total_carro(request):
    total=0
    if request.user.is_authenticated:
        if "carro" in request.session:
            
            for key,value in request.session["carro"].items():
                total=total+(float(value["precio"]))
                
            if total !=0:

                if total<200:
                    total=total+150
            
            
            


            
                
                    
                 
                
    return {"total_carro":total}


