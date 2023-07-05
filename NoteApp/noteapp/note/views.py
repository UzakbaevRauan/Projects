from django.shortcuts import render ,redirect
from .models  import Document

# Create your views here.
# Create your views here.
def editor(request):
    docid = int(request.GET.get('docid',0))
    documents = Document.objects.all()

    if request.method == 'POST':
        docid = int(request.POST.get('docid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if docid > 0:
            document = Document.objects.get(pk=docid)
            document.title = title
            document.content = content
            document.save()

            return redirect('/?docid=%i' % docid)
        else:
            document = Document.objects.create(title=title, content=content)

            return redirect('/?docid=%i' % document.id)

    if docid >0:
        document = Document.objects.get(pk=docid)
    else:
        document =''
        
    context = {
        'docid':docid,
        'documents':documents,
        'document':document
    }
    return render(request, 'editor.html', context)

def delete_document(request,id):
    document= Document.objects.get(pk=id)
    document.delete()
    return redirect('/?id=0')

