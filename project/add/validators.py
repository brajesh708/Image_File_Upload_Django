from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _ 
import os
from django.core.exceptions import ValidationError

def validate_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.docx', '.doc', '.txt']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Invalid file extension'))
    
    file_size = value.size
    if file_size > 1048576: # 1MB
        raise ValidationError(_('File too large (1MB)'))
    
def validate_image(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Invalid file extension'))
    
    file_size = value.size
    max_image_size = 1 * 1024 * 1024 # 5MB
    if file_size > max_image_size:
        raise ValidationError(_('File too large (5MB)'))
    
    
    
    