# chords_app/models.py

from django.db import models

class Key(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Chord(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()  # If you still want this field in Chord
    key = models.ForeignKey(Key, related_name='chords', on_delete=models.CASCADE)

class ChordImage(models.Model):
    chord = models.ForeignKey(Chord, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='chord_images/')

    def __str__(self):
        return f"Image for {self.chord.name}"
