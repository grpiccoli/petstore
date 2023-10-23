# Import required libraries
import requests  # For making HTTP requests
import json  # For JSON parsing
import unittest  # For unit testing

# Function to fetch available pets from PetStore API
def fetch_available_pets():
    url = 'https://petstore.swagger.io/v2/pet/findByStatus'  # API endpoint
    params = {'status': 'available'}  # Query parameter
    response = requests.get(url, params=params)  # HTTP GET request
    
    # Check if request was successful
    if response.status_code == 200:
        return response.json()  # Parse and return JSON response
    else:
        return None  # Return None if request failed

# Function to sort a list of pets
def sort_pets(pets):
    # Sort by category name and pet name in reverse order
    return sorted(pets, key=lambda x: (
        x['category']['name'] if 'category' in x and 'name' in x['category'] else '', 
        x['name'] if 'name' in x else ''), 
        reverse=True)

# Function to sort and print a list of pets
def sort_and_print_pets(pets):
    sorted_pets = sort_pets(pets)  # Sort the pets
    current_category = None  # Keep track of current category
    new_pets = []  # List to store new pet details
    
    # Loop through sorted pets
    for pet in sorted_pets:
        # Extract category name, default to 'Unknown' if not available
        category = pet['category']['name'] if 'category' in pet and 'name' in pet['category'] else 'Unknown'
        
        # Print new category name if it differs from current category
        if category != current_category:
            print(f"Category: {category}")
            current_category = category
        
        # Extract pet name, default to 'Unknown' if not available
        pet_name = pet['name'] if 'name' in pet else 'Unknown'
        print(f"  Pet: {pet_name}")  # Print pet name
        
        # Append new pet details to list
        new_pets.append({'name': pet_name, 'category': category})
    
    return new_pets  # Return list of new pet details

# Unit testing class
class TestPetFunctions(unittest.TestCase):
    
    # Test sort_pets and sort_and_print_pets functions
    def test_sort_pets(self):
        # Sample list of pets
        pets = [
            {'name': 'Dog1', 'category': {'name': 'Dogs'}},
            {'name': 'Cat1', 'category': {'name': 'Cats'}},
            {'name': 'Dog2', 'category': {'name': 'Dogs'}},
            {}
        ]
        
        # Test if sort_pets function maintains the list length
        sorted_pets = sort_pets(pets)
        self.assertEqual(len(sorted_pets), len(pets))

        # Test if sort_and_print_pets function sorts correctly
        new_pets = sort_and_print_pets(pets)
        self.assertEqual(new_pets[0]['name'], 'Dog2')
        self.assertEqual(new_pets[1]['name'], 'Dog1')
        self.assertEqual(new_pets[2]['name'], 'Cat1')
        self.assertEqual(new_pets[3]['name'], 'Unknown')

# Main function
if __name__ == '__main__':
    pets = fetch_available_pets()  # Fetch available pets
    if pets:  # If pets are available
        sort_and_print_pets(pets)  # Sort and print the list of pets
