from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserTestCase(TestCase):

    def test_create_user(self):
        user = User.objects.create(
            username='testuser', 
            email='testuser@email.com', 
            password='testpass123'
        )
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.is_active) 
        self.assertFalse(user.is_staff) 
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            username='testuser', 
            email='testuser@email.com', 
            password='testpass123'
        )
        self.assertEqual(admin_user.username,"testuser")
        self.assertTrue(admin_user.is_active) 
        self.assertTrue(admin_user.is_staff) 
        self.assertTrue(admin_user.is_superuser)