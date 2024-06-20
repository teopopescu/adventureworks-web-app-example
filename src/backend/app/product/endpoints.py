from typing import Optional, List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from src.backend.settings.db import get_db
from src.backend.app.product.services import ProductService
from src.backend.app.product.schemas import productResponse

"""  
CRUD PRODUCT
Fetch product category joined with product
Fetch product model, product review, product sub category
Products in the inventory within a timeline
CRUD product review
Add query parameters
Add path parameters
Handle errors
Use nested models
Use cookies
Use middleware
Use asynchronous request to compute statistics with Celery, Redis and Flower
Add unit and integration testing

Sales
- CRUD store
- Compute sales in a time range
- Compute sales for a store


Purchases
- CRUD Purchases
- CRUD Vendor

Make 2 microservices talk to each other



"""



product_router = APIRouter()


@product_router.get("/products/{product_id}")
async def get_product(
    product_id: str,
    db: Session = Depends(get_db),
    limit: Optional[int] = 1000,
):
    product = ProductService.get_by_id(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=404, detail=f"The product {product_id} doesn't exist"
        )
    
    return {
            "job_title": product.nationalidnumber,
            "national_id_number": product.jobtitle
        }

@product_router.post("/products/{product_id}", response_model=AddProduct)
async def add_product(
    product_id: str,
    entry: AddProduct, 
    db: Session = Depends(get_db),
    limit: Optional[int] = 1000,
):
    product = ProductService.get_by_id(db=db, product_id=product_id)
    if not product:
        raise HTTPException(
            status_code=404, detail=f"The product {product_id} doesn't exist"
        )
    
    ids = [item.national_id_number for item in entry.product_added]

    if len(product) == 0:
        raise HTTPException(status_code=404, detail=f"No product found")


    group = ProductService.create_product(
        db=db, name=entry.name, description=entry.description
    )
    ProductService.add_product(db, group, entry.experiments)
    return {"success": True, "product_added": entry.national_id_number}




@product_router.put(
    "/product/{product_id}",
    response_model=UpdateProduct,
)
async def update_product(
    destination_product_id: int,
    payload: UpdateProduct,
    db: Session = Depends(get_db),
):
    destination_product_id = ProductService.get_by_id(db=db, product_id=destination_product_id)

    if not destination_product_id:
        raise HTTPException(
            status_code=404,
            detail=f"The product {destination_product_id} doesn't exist",
        )

    experiments_groups_list = {p.experiment_id: p.group_id for p in payload.experiments}
    ProductService.update_by_product_id(
            db=db, product=payload.product_id
        )
    
    # for entry in payload.experiments:

    #     product = ProductService.get_by_id(db, product_id=entry.product_id)

    #     if not group:
    #         raise HTTPException(
    #             status_code=404, detail=f"The group: {entry.group_id} doesn't exists"
    #         )

    #     ProductService.update_by_product_id(
    #         db=db, experiment=payload.experiments, from_group=group, to_group=destination_group
    #     )

    return {
        "success": True,
        "product_id": destination_product_id.to_json(),
    }

@product_router.delete(
    "/product/{group_id}", response_model=DeleteProductResponse
)
async def delete_experiments_from_the_group(
    group_id: int,
    entry: DeleteProductRequest,
    db: Session = Depends(get_db),
):
    product = ProductService.get_by_id(db=db, group_id=group_id)

    if not product:
        raise HTTPException(
            status_code=404, detail=f"The product: {product} doesn't exist"
        )

    ProductService.delete_product(db, product, entry.experiments)
    return {"success": True, "product_removed": entry.product}




""" 
 production     | billofmaterials                       | table | postgres
 production     | culture                               | table | postgres
 production     | document                              | table | postgres
 production     | illustration                          | table | postgres
 production     | location                              | table | postgres
 production     | product                               | table | postgres
 production     | productcategory                       | table | postgres
 production     | productcosthistory                    | table | postgres
 production     | productdescription                    | table | postgres
 production     | productdocument                       | table | postgres
 production     | productinventory                      | table | postgres
 production     | productlistpricehistory               | table | postgres
 production     | productmodel                          | table | postgres
 production     | productmodelillustration              | table | postgres
 production     | productmodelproductdescriptionculture | table | postgres
 production     | productphoto                          | table | postgres
 production     | productproductphoto                   | table | postgres
 production     | productreview                         | table | postgres
 production     | productsubcategory                    | table | postgres
 production     | scrapreason                           | table | postgres
 production     | transactionhistory                    | table | postgres
 production     | transactionhistoryarchive             | table | postgres
 production     | unitmeasure                           | table | postgres
 production     | workorder                             | table | postgres
 production     | workorderrouting                      | table | postgres

CRUD PRODUCT
Fetch product category joined with product
Fetch product model, product review, product sub category
Products in the inventory within a timeline
CRUD product review
Add query parameters
Add path parameters
Handle errors
Use nested models 

"""
