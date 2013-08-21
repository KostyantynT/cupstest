# Create your views here.
from contacts.models import Contact
from django.views import generic
from django.forms.models import modelform_factory
from django.core.urlresolvers import reverse

class IndexView(generic.DetailView):
    model = Contact
    template_name='contacts/index.html'
    
    def get_queryset(self):
        if self.kwargs.get("pk") is None:
            self.kwargs["pk"]=1
        return Contact.objects.filter(pk=self.kwargs["pk"])

class UpdateContactView(generic.UpdateView):
    model = Contact
    form_class = modelform_factory(model=Contact)
    #form_class = ContactForm
    template_name = 'contacts/edit.html'

    def get_success_url(self):
        return reverse('index')
        
#     def modelform_valid(self, modelform):
#         pk   = self.kwargs.get("pk")
#         old = Contact.objects.get(pk=pk).picture
#         #if old.
#         self.modelform_object = modelform.save()
#         if self.modelform_object.picture_url:
#             pass#
#         return redir(self.success_url)