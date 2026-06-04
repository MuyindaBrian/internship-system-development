from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from internships.models import Internship, InternshipApplication
from maintenance.models import MaintenanceRequest
from aob.models import AOBRequest

User = get_user_model()


class Command(BaseCommand):
    help = 'Populate database with sample data'

    def handle(self, *args, **options):
        self.stdout.write('Starting to populate database with sample data...')

        # Create admin user
        if not User.objects.filter(email='admin@example.com').exists():
            admin = User.objects.create_user(
                email='admin@example.com',
                username='admin@example.com',
                name='Admin User',
                password='admin123',
                user_type='admin'
            )
            self.stdout.write(self.style.SUCCESS('✓ Admin user created'))
        else:
            admin = User.objects.get(email='admin@example.com')

        # Create company users
        companies = [
            {'email': 'company1@techcorp.com', 'name': 'Tech Corp', 'company': 'Tech Corp'},
            {'email': 'company2@fintech.com', 'name': 'FinTech Inc', 'company': 'FinTech Inc'},
        ]

        company_users = []
        for company_data in companies:
            if not User.objects.filter(email=company_data['email']).exists():
                user = User.objects.create_user(
                    email=company_data['email'],
                    username=company_data['email'],
                    name=company_data['name'],
                    password='company123',
                    user_type='company',
                    company_name=company_data['company']
                )
                company_users.append(user)
                self.stdout.write(self.style.SUCCESS(f"✓ Company user created: {company_data['name']}"))
            else:
                company_users.append(User.objects.get(email=company_data['email']))

        # Create student users
        students = [
            {'email': 'student1@university.edu', 'name': 'Alice Johnson'},
            {'email': 'student2@university.edu', 'name': 'Bob Smith'},
            {'email': 'student3@university.edu', 'name': 'Charlie Brown'},
        ]

        student_users = []
        for student_data in students:
            if not User.objects.filter(email=student_data['email']).exists():
                user = User.objects.create_user(
                    email=student_data['email'],
                    username=student_data['email'],
                    name=student_data['name'],
                    password='student123',
                    user_type='student',
                    phone='555-0123'
                )
                student_users.append(user)
                self.stdout.write(self.style.SUCCESS(f"✓ Student user created: {student_data['name']}"))
            else:
                student_users.append(User.objects.get(email=student_data['email']))

        # Create internships
        internships_data = [
            {
                'title': 'Summer Web Development Internship',
                'description': 'Develop responsive web applications using React and Django',
                'company': 'Tech Corp',
                'duration': '3 months',
                'status': 'active'
            },
            {
                'title': 'Mobile App Development Internship',
                'description': 'Build native and cross-platform mobile applications',
                'company': 'Tech Corp',
                'duration': '3 months',
                'status': 'active'
            },
            {
                'title': 'Financial Software Internship',
                'description': 'Work on fintech platform development and optimization',
                'company': 'FinTech Inc',
                'duration': '6 months',
                'status': 'active'
            },
            {
                'title': 'DevOps Engineering Internship',
                'description': 'Learn about cloud infrastructure and CI/CD pipelines',
                'company': 'Tech Corp',
                'duration': '3 months',
                'status': 'pending'
            },
        ]

        for internship_data in internships_data:
            if not Internship.objects.filter(title=internship_data['title']).exists():
                internship = Internship.objects.create(
                    title=internship_data['title'],
                    description=internship_data['description'],
                    company=internship_data['company'],
                    duration=internship_data['duration'],
                    status=internship_data['status'],
                    created_by=admin
                )
                self.stdout.write(self.style.SUCCESS(f"✓ Internship created: {internship_data['title']}"))
            else:
                internship = Internship.objects.get(title=internship_data['title'])

            # Create applications for students
            for student in student_users[:2]:
                if not InternshipApplication.objects.filter(
                    internship=internship,
                    applicant=student
                ).exists():
                    InternshipApplication.objects.create(
                        internship=internship,
                        applicant=student,
                        status='pending'
                    )

        self.stdout.write(self.style.SUCCESS('✓ Internships and applications created'))

        # Create maintenance requests
        maintenance_data = [
            {'room': 'Lab 101', 'issue': 'Air conditioner not working'},
            {'room': 'Room 205', 'issue': 'Broken window'},
            {'room': 'Library Ground Floor', 'issue': 'Damaged chair'},
        ]

        for maint_data in maintenance_data:
            if not MaintenanceRequest.objects.filter(
                room=maint_data['room'],
                issue=maint_data['issue']
            ).exists():
                MaintenanceRequest.objects.create(
                    room=maint_data['room'],
                    issue=maint_data['issue'],
                    status='pending',
                    requested_by=student_users[0]
                )

        self.stdout.write(self.style.SUCCESS('✓ Maintenance requests created'))

        # Create AOB requests
        aob_data = [
            {
                'title': 'Internship Stipend Payment',
                'description': 'When will the stipend for my internship be processed?',
                'category': 'payment'
            },
            {
                'title': 'Internship Extension Request',
                'description': 'Can I extend my internship by another month?',
                'category': 'allocation'
            },
            {
                'title': 'Technical Support Needed',
                'description': 'Need help with VPN access to company systems',
                'category': 'support'
            },
        ]

        for aob_item in aob_data:
            if not AOBRequest.objects.filter(title=aob_item['title']).exists():
                AOBRequest.objects.create(
                    title=aob_item['title'],
                    description=aob_item['description'],
                    category=aob_item['category'],
                    status='pending',
                    submitted_by=student_users[0]
                )

        self.stdout.write(self.style.SUCCESS('✓ AOB requests created'))

        self.stdout.write(self.style.SUCCESS(self.style.HTTP_SUCCESS(
            '\n✓ Database populated successfully!\n'
            'Test Credentials:\n'
            '  Admin: admin@example.com / admin123\n'
            '  Student: student1@university.edu / student123\n'
            '  Company: company1@techcorp.com / company123\n'
        )))
