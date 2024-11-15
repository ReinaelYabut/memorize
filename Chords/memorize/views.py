# chords_app/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import JsonResponse

def key_list(request):
    keys = Key.objects.all()
    return render(request, 'key_list.html', {'keys': keys})

def chord_list(request, key_id):
    key = get_object_or_404(Key, id=key_id)
    chords = Chord.objects.filter(key=key)

    if request.method == 'POST':
        chord_form = ChordForm(request.POST)
        if chord_form.is_valid():
            chord = chord_form.save(commit=False)
            chord.key = key  # Associate the chord with the key
            chord.save()

            # Handle images
            image_files = request.FILES.getlist('images')
            for image_file in image_files:
                chord_image = ChordImage(chord=chord, image=image_file)  # Associate image with the new chord
                chord_image.save()

            return redirect('chord_list', key_id=key.id)
    else:
        chord_form = ChordForm()

    return render(request, 'chord_list.html', {'key': key, 'chords': chords, 'chord_form': chord_form})

@require_POST  # This decorator ensures the view only accepts POST requests
def add_key(request):
    if request.method == 'POST':
        key_name = request.POST.get('key_name')
        if key_name:  # Make sure key name is not empty
            Key.objects.create(name=key_name)  # Create a new key instance
            messages.success(request, f'Key "{key_name}" added successfully!')
        else:
            messages.error(request, 'Key name cannot be empty.')
    return redirect('key_list')  # Redirect to the key list after adding


def add_chord(request):
    if request.method == 'POST':
        form = ChordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('key_list')  # Redirect after adding a chord
    else:
        form = ChordForm()
    return render(request, 'add_chord.html', {'form': form})

def add_chord_image(request):
    if request.method == 'POST':
        form = ChordImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('key_list')  # Redirect after adding an image
    else:
        form = ChordImageForm()
    return render(request, 'add_chord_image.html', {'form': form})

def flashcard_game(request, key_id):
    # Get the Key object based on the key_id
    key = get_object_or_404(Key, id=key_id)
    
    # Retrieve all chords associated with this key
    chords = key.chords.all()  # Assuming a ForeignKey relationship from Chord to Key
    
    # Render the flashcard template with the chords
    return render(request, 'flashcard_game.html', {
        'key': key,
        'chords': chords,
    })

def flashcard_data(request, key_id):
    # Fetch the Key object
    key = Key.objects.get(id=key_id)
    
    # Fetch all Chords associated with the Key
    chords = key.chords.all()  # 'chords' is the related_name from the ForeignKey in Chord

    # Prepare the response data
    chord_data = []
    for chord in chords:
        # Gather image URLs for each chord
        images = [image.image.url for image in chord.images.all()]  # Fetch image URLs

        chord_data.append({
            'name': chord.name,
            'description': chord.description,
            'images': images,  # Include the list of image URLs
        })

    return JsonResponse({'chords': chord_data})