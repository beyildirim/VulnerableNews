from fastapi import APIRouter
from api.v1.route_homepage import router as homepage_router
from api.v1.route_users import router as users_router
from api.v1.route_posts import router as posts_router

api_router = APIRouter()
api_router.include_router(homepage_router, prefix="", tags=["homepage"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
api_router.include_router(posts_router, prefix="/posts", tags=["posts"])