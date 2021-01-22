from django.shortcuts import render  
from firstproject.forms import food 
  
def add(response):  

    if response.method == 'POST':
        add_obj = food(response.POST) 
        if add_obj.is_valid():
            apple = add_obj.cleaned_data['apple']
            orange = add_obj.cleaned_data['orange']
            banana = add_obj.cleaned_data['banana']
            onion = add_obj.cleaned_data['onion']
            carrot = add_obj.cleaned_data['carrot']
            rice =  add_obj.cleaned_data['rice']
            fish = add_obj.cleaned_data['fish']
            stretching = add_obj.cleaned_data['stretching']
            pushups = add_obj.cleaned_data['pushups']
            lifting = add_obj.cleaned_data['lifting']
            walking = add_obj.cleaned_data['walking']
            running = add_obj.cleaned_data['running']

            
            apple_cal=apple*0.52
            orange_cal=orange*0.47
            banana_cal=banana*0.89
            onion_cal=onion*0.40
            carrot_cal=carrot*0.41
            rice_cal=rice*1.3
            fish_cal=fish*2.06
            a=apple_cal+orange_cal+banana_cal+onion_cal+carrot_cal+fish_cal+rice_cal
            a=round(a,2)

            apple_fat=apple*0.002
            orange_fat=orange*0.001
            banana_fat=banana*0.003
            onion_fat=onion*0.001
            carrot_fat=carrot*0.002
            rice_fat=rice*0.003
            fish_fat=fish*0.12
            f=apple_fat+orange_fat+banana_fat+onion_fat+carrot_fat+rice_fat+fish_fat
            f=round(f,2)

            apple_A=apple*0.54
            orange_A=orange*2.25
            banana_A=banana*0.64
            onion_A=onion*0.02
            carrot_A=carrot*167.06
            rice_A=rice*0
            fish_A=fish*0.5
            A=apple_A+orange_A+banana_A+onion_A+carrot_A+rice_A+fish_A
            A=round(A,2)


            apple_C=apple*0.046
            orange_C=orange*0.532
            banana_C=banana*0.087
            onion_C=onion*0.074
            carrot_C=carrot*0.059
            rice_C=rice*0
            fish_C=fish*0.037
            C=apple_C+orange_C+banana_C+onion_C+carrot_C+rice_C+fish_C
            C=round(C,2)


            apple_calc=apple*0.06
            orange_calc=orange*0.40
            banana_calc=banana*0.05
            onion_calc=onion*0.23
            carrot_calc=carrot*0
            rice_calc=rice*0.1
            fish_calc=fish*0.15
            calc=apple_calc+orange_calc+banana_calc+onion_calc+carrot_calc+rice_calc+fish_calc
            calc=round(calc,2)



            stretch_cal=stretching*1.2
            push_cal=pushups*7
            lift_cal=lifting*1.6
            walk_cal=walking*0.04
            run_cal=running*11.4
            burnt=stretch_cal+push_cal+lift_cal+walk_cal+run_cal
            burnt=round(burnt,2)


            return render(response, 'output.html', {'calories':a ,'fats':f,'VITAMIN_A':A,'VITAMIN_C':C,'CALCIUM':calc,'BURNT':burnt})

        else:
            return render(response, 'vicky.html', {'form': add_obj})

    else:
        add_obj = food() 
        return render(response, 'vicky.html', {'form': add_obj})