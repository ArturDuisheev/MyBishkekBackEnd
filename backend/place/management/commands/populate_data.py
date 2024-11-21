import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ...models import Category, Place, PlaceImage

fake = Faker()

class Command(BaseCommand):
    help = "Populate the database with fake data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting data generation...")

        # Create categories
        categories = []
        for _ in range(10):
            category, created = Category.objects.get_or_create(
                name=fake.word().capitalize()
            )
            categories.append(category)

        self.stdout.write(f"Created {len(categories)} categories.")

        # Create users
        users = []
        for _ in range(10):
            user = User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password123"
            )
            users.append(user)

        self.stdout.write(f"Created {len(users)} users.")

        # Create place images
        place_images = []
        for _ in range(20):
            image = PlaceImage.objects.create(
                image=fake.image_url()  # Use fake image URLs; replace with actual paths if required
            )
            place_images.append(image)

        self.stdout.write(f"Created {len(place_images)} place images.")

        # Create places
        for _ in range(50):
            place = Place.objects.create(
                name=fake.company(),
                avg_price=random.uniform(100, 5000),
                avg_rating=random.uniform(1, 5),
                coordinates_x=random.uniform(-180, 180),
                coordinates_y=random.uniform(-90, 90),
                description=fake.text(),
                phone=fake.phone_number(),
                whatsapp=fake.phone_number(),
                instagram=fake.url(),
                address=fake.address(),
                created_by=random.choice(users)
            )

            # Attach random images and categories
            place.images.set(random.sample(place_images, random.randint(1, 5)))
            place.categories.set(random.sample(categories, random.randint(1, 3)))

            self.stdout.write(f"Created place: {place.name}")

        self.stdout.write("Data generation completed.")