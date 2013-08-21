# from django import forms
# from contacts.models import Contact
# 
# class ContactForm(forms.ModelForm):
#     success_url = '/contacts/'
#     class Meta: # model must be in the Meta class
#         model = Contact
#     
# #     def form_valid(self, form):
# #         #Insert upload file storing and change filepath for model
# #         #form.instance.created_by = self.request.user
# #         return super(UpdateContactView, self).form_valid(form)
#     
# #     def get_context_data(self, **kwargs):
# #         context = super(ItemUpdateView, self).get_context_data(**kwargs)
# #         item = context['object']
# #         # Dont' create any extra forms when showing an update view
# #         PictureFormSet = formset_factory(PictureForm, extra=0)
# #         return {'form': kwargs['form'],
# #                 'picture_formset': UploadFormSet(initial = [ model_to_dict(a) for pic in item.pictures.all()])}
# #     def post(self, request, *args, **kwargs):
# #        self.object = self.get_object()
# #        item_form = ItemCreateForm(request.POST, instance=self.object)
# #        if item_form.is_valid():
# #            item = item_form.save(commit=False)
# #            item.save()
# #            # How do I update the pictures? 
# 
# #     def __init__(self, *args, **kwargs):
# #         if kwargs.get('instance'):
# #             name = kwargs['instance'].name
# #             surname = kwargs['instance'].surname
# #             birthdate = kwargs['instance'].birthdate
# #             bio = kwargs['instance'].bio
# #             contactdetails = kwargs['instance'].contactdetails
# #             photo = kwargs['instance'].photo
# #         return super(ContactForm, self).__init__(*args, **kwargs)
# #     