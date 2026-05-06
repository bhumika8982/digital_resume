from fastapi import HTTPException
from models.contact_model import ContactModel
from schemas.contact_schema import ContactForm

class ContactController:
    @staticmethod
    async def save_contact(contact: ContactForm):
        try:
            contact_id = await ContactModel.create_contact(contact)
            return {"success": True, "message": "Message sent successfully!", "id": contact_id}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    async def fetch_all_contacts():
        try:
            contacts = await ContactModel.get_all_contacts()
            return {"success": True, "data": contacts}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
