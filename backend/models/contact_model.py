from database import contact_collection
from schemas.contact_schema import ContactForm

class ContactModel:
    @staticmethod
    async def create_contact(contact: ContactForm):
        new_contact = await contact_collection.insert_one(contact.model_dump())
        return str(new_contact.inserted_id)

    @staticmethod
    async def get_all_contacts():
        contacts = []
        cursor = contact_collection.find({})
        async for document in cursor:
            document["_id"] = str(document["_id"])
            contacts.append(document)
        return contacts
