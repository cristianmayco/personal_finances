from django.core.exceptions import ValidationError
from django.test import TestCase
from core import models


class BillTestModel(TestCase):
    # water, light, market, personal, gifts,
    # repairs, others

    def test_create_new_bill_without_payday(self):
        """Test creating a new bill without payday"""
        bill = models.Bill.objects.create(
            type='W',
            description='Company water bill',
            amount=150.00,
            due_date='2020-08-25',
        )

        self.assertEqual(models.Bill.objects.get(type=bill.type), bill)

    def test_create_new_bill_without_payday_and_active(self):
        """Test creating a new bill without payday and active false"""
        with self.assertRaises(ValueError):
            bill = models.Bill.objects.create(
                type='W',
                description='Company water bill',
                amount=150.00,
                due_date='2020-08-25',
                active=False
            )

    def test_create_new_bill_sucessful(self):
        """Test creating a new bill is sucessful"""
        bill = models.Bill.objects.create(
            type='W',
            description='Company water bill',
            amount=150.00,
            due_date='2020-08-25',
            payday='2020-08-30',
            active=False
        )

        self.assertEqual(models.Bill.objects.get(type=bill.type), bill)

    def test_bill_str(self):
        """Test bill string representation"""
        bill = models.Bill.objects.create(
            type='W',
            description='Company water bill',
            amount=150.00,
            due_date='2020-08-25',
            payday='2020-08-30',
            active=False
        )

        self.assertEqual(str(bill), bill.type)
