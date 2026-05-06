from fastapi import APIRouter
from controllers.contact_controller import ContactController
from schemas.contact_schema import ContactForm

router = APIRouter(prefix="/api/contact", tags=["Contact"])

@router.post("/")
async def submit_contact(contact: ContactForm):
    return await ContactController.save_contact(contact)

@router.get("/")
async def get_contacts():
    return await ContactController.fetch_all_contacts()
