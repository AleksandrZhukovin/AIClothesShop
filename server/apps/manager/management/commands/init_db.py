from django.core.management.base import BaseCommand

from server.apps.manager.services.db_init import DatabaseInitializer


class Command(BaseCommand):
    help = "Initialize database with predefined data"

    def handle(self, *args, **options):
        self.stdout.write("Initializing database...")

        try:
            initializer = DatabaseInitializer()
            results = initializer.initialize_all()

            for model_name, result in results.items():
                count = result["created_count"]
                if count > 0:
                    self.stdout.write(
                        self.style.SUCCESS(f"Created {count} new {model_name}(s)")
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"No new {model_name}s needed to be created")
                    )

            self.stdout.write(self.style.SUCCESS("Successfully initialized database!"))

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"Error initializing database: {str(e)}")
            )
