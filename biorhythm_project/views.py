from django.shortcuts import render
from django.http import JsonResponse
import math
from datetime import datetime,date



def index(request):
    return render(request,'index.html')

def show_result(request, data):
    return render(request,'index.html',data)

def calculate_biorhythm(request):
    if request.method == 'POST':
        # Extract birthdate from request data
        birthdate_str = request.POST.get('birthdate')
        if birthdate_str:
            try:
                # Parse birthdate string into datetime object
                birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
                target_date = datetime.now()
                print ((target_date-birthdate).days)
                print(math.sin(2*math.pi*10000/23)*100)
                # Calculate biorhythm cycles
                physical = math.sin(2 * math.pi * (target_date - birthdate).days / 23) * 100
                emotional = math.sin(2 * math.pi * (target_date - birthdate).days / 28) * 100
                intellectual = math.sin(2 * math.pi * (target_date - birthdate).days / 33) * 100

                # Create JSON response with biorhythm data
                data = {
                    'physical': physical,
                    "physical_cycle": """This cycle reflects a person's physical energy, strength, and coordination. When the physical cycle is high, individuals may feel more energetic, alert, and capable of physical activity. Conversely, when the physical cycle is low, they may experience fatigue, weakness, or reduced physical performance""",

                    'emotional': emotional,
                    "emotional_cycle": """ The emotional cycle relates to a person's mood, emotional stability, and sensitivity. During high points in the emotional cycle, individuals may feel emotionally balanced, positive, and resilient. However, during low points, they may be more prone to mood swings, irritability, or emotional distress""",

                    'intellectual': intellectual,
                    "intellectual_cycle": """The intellectual cycle influences cognitive abilities such as problem-solving, decision-making, and creativity. When the intellectual cycle is high, individuals may experience increased mental clarity, focus, and productivity. Conversely, during low points, they may struggle with concentration, memory recall, or mental agility.
                                        Interpreting the results involves considering how these cycles may align with daily experiences and activities."""

                }
                return show_result(request, data)


            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Please use YYYY-MM-DD.'}, status=400)
        else:
            return JsonResponse({'error': 'Birthdate is required.'}, status=400)
    else:
        return JsonResponse({'error': 'Unsupported request method.'}, status=405)
