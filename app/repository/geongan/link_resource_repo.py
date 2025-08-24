from sqlalchemy.orm import Session

from app.models.geongan.link_resource import LinkResource
from app.schemas.geongan.link_resource import LinkResourceCreate


def create_link_resource(db: Session, link_resource_in: LinkResourceCreate):
    db_obj = LinkResource(**link_resource_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get_all_link_resource(db: Session):
    return db.query(LinkResource).all()


def get_link_resource(db: Session, link_id: int):
    return db.query(LinkResource).filter(LinkResource.id == link_id).first()


def delete_link_resource(db: Session, link_id: int):
    db.query(LinkResource).filter(LinkResource.id == link_id).delete()
    db.commit()

