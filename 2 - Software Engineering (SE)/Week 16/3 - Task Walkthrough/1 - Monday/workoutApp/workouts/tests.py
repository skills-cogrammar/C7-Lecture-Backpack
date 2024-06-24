from django.test import TestCase
from django.urls import reverse
from .models import Workout


# class WorkoutTest(TestCase):
    
#     # If your tests aren't passing for any strange reason try this instaed of 
#     # setUp()
#     @classmethod
#     def setUpTestData(cls):
#         Workout.objects.create(
#             name='Workout 1', description='Description 1', sets=10, creator="Test")

#     # def setUp(self):
#     #     Workout.objects.create(
#     #         name='Workout 1', description='Description 1', sets=10, creator="Test")
        
#     def test_workout_has_name(self):
#         workout = Workout.objects.get(id=1)
#         self.assertEqual(workout.name, 'Workout 1')

#     def test_workout_has_description(self):
#         workout = Workout.objects.get(id=1)
#         self.assertEqual(workout.description, 'Description 1')

#     def test_workout_has_sets(self):
#         workout = Workout.objects.get(id=1)
#         self.assertEqual(workout.sets, 10)

#     def test_workout_has_creator(self):
#         workout = Workout.objects.get(id=1)
#         self.assertEqual(workout.creator, 'Test')

class WorkoutViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Workout.objects.create(
        name='Workout 1', description='Description 1', sets=10, creator="Test")

        Workout.objects.create(
        name='Workout 1', description='Description 1', sets=10, creator="Test")
        

    def test_workout_get_all_returns_all_workouts(self):
        response = self.client.get(reverse('workouts'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Workout 1')

    def test_workout_get_returns_workout(self):
        workout = Workout.objects.get(id=1)
        response = self.client.get(reverse('workout', args=[workout.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Workout 1')


    def test_delete_should_remove_item(self):
        workouts = Workout.objects.all()
        init_length = workouts.count()

        workout = Workout.objects.get(id=1)

        response = self.client.get(reverse('delete_workout', args=[workout.id]))

        # Final length check 
        final_length = Workout.objects.all().count()
        
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(init_length, final_length)




    
