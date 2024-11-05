from rest_framework import serializers

from student.models.student_model import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        exclude = ['gender', 'url_picture']
