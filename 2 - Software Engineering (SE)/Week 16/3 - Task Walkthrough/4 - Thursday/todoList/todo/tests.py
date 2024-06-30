from django.test import TestCase
from django.urls import reverse
from .models import Todo

class TodoTest(TestCase):

    # If your tests are throwing an error when you have more than 1 test try this
    # @classmethod
    # def setUpTestData(cls):
    #     Todo.objects.create(title="Test Todo", 
    #                         description="This is a test todo",
    #                         is_completed=False,
    #                         created_by="Test User")

    def setUp(self) -> None:
        Todo.objects.create(title="Test Todo", 
                            description="This is a test todo",
                            is_completed=False,
                            created_by="Test User")
        
    def test_todo_create_has_title(self):
        todo = Todo.objects.get(id=1)

        self.assertEqual(todo.title, "Test Todo")

    def test_todo_create_has_description(self):
        todo = Todo.objects.get(id=1)

        self.assertEqual(todo.description, "This is a test todo")

class TodoViewTest(TestCase):
    def setUp(self) -> None:
        Todo.objects.create(title="Test Todo", 
                            description="This is a test todo",
                            is_completed=False,
                            created_by="Test User")
        
    def test_get_all_returns_correct_values(self):
        response = self.client.get(reverse('todos'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_get_returns_correct_values(self):
        todo = Todo.objects.get(id=1)
        response = self.client.get(reverse('todo', args=[todo.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Todo")

    def test_create_adds_todo_to_database(self):
        start_counter = Todo.objects.count()        

        response = self.client.post(reverse('create_todo'), {
            'title': 'New Todo',
            'description': 'This is a new todo',
            'is_completed': False,
            'created_by': 'Test User'
        })

        final_count = Todo.objects.count()        

        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(start_counter, final_count)

        
    
