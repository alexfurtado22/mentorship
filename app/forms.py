from django import forms

from app.models import CoMentor, Mentorship


class CreateMentorForm(forms.ModelForm):
    class Meta:
        model = Mentorship
        fields = [
            "name",
            "picture",
            "company",
            "status",
            "comentor",
            "content",
        ]  # 👈 Removed 'user'

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)  # 👈 Grab user passed from view
        super().__init__(*args, **kwargs)

        self.fields["status"].empty_label = "Select status"
        self.fields["comentor"].empty_label = "Select co-mentor"

        # Optionally, you can add custom validation or modify field queries
        if user:
            self.fields["comentor"].queryset = CoMentor.objects.filter(user=user)


class CoMentorForm(forms.ModelForm):
    class Meta:
        model = CoMentor
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {
                "class": "block w-full rounded-md border border-border focus:ring-emerald-500 focus:border-emerald-500 p-2",
                "placeholder": "Enter co-mentor name",
            }
        )
