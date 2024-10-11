from django.shortcuts import render
from .forms import TextFileForm
import random

# Create your views here.
def scramble_text(text):
    words = text.split()
    scrambled_words = []
    for word in words:
        if len(word) > 3:
            word = word[0] + ''.join(random.sample(word[1:-1], len(word) - 2)) + word[-1]
        scrambled_words.append(word)
    scrambled_text = ' '.join(scrambled_words)
    return scrambled_text

def index(request):
    print("Widok index został wywołany")  # Debugowanie
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            text = file.read().decode('utf-8')
            scrambled_text = scramble_text(text)
            print("Przekierowanie na result.html")  # Debugowanie
            return render(request, 'result.html', {'scrambled_text': scrambled_text})
    else:
        form = TextFileForm()
    return render(request, 'index.html', {'form': form})
