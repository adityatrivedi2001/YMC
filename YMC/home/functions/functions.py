def handle_uploaded_file(f):
    with open('YMC/home/assets/upload'+f.name+'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunks)
