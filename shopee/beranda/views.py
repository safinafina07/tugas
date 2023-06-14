from django.shortcuts import render


def beranda (request):
    judul= [ "pesanan", "dikemas", "dikirim" ]
    pemilik= "safinatunnajah"

    konteks={
        'title':judul,
        'pemilik':pemilik,
    }

    return render(request,'beranda.html', konteks )

