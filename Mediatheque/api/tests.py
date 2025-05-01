from rest_framework.test import APITestCase
from rest_framework import status
from .models import *
from datetime import date

class AuteurTestCase(APITestCase):
    def setUp(self):
        self.user = Lecteur.objects.create_user(username="test", password="mdptest", date_naissance=date(2000,1,1))
        self.client.login(username="test", password="mdptest")

        self.auteur = Auteur.objects.create(nom="test")

    def test_list_auteurs(self):
        res = self.client.get("/api/auteurs/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_auteurs(self):
        res = self.client.post("/api/auteurs/", {"nom":"test"}, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Auteur.objects.count(), 2)

    def test_detail_auteurs(self):
        res = self.client.get(f"/api/auteurs/{self.auteur.id}/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["nom"], "test")

    def test_update_auteurs(self):
        res = self.client.put(f"/api/auteurs/{self.auteur.id}/", {"nom":"nouvtest"}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.auteur.refresh_from_db()
        self.assertEqual(self.auteur.nom, "nouvtest")

    def test_delete_auteurs(self):
        res = self.client.delete(f"/api/auteurs/{self.auteur.id}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Auteur.objects.count(), 0)

class TagTestCase(APITestCase):
    def setUp(self):
        self.user = Lecteur.objects.create_user(username="test", password="mdptest", date_naissance=date(2000,1,1))
        self.client.login(username="test", password="mdptest")

        self.tag = Tag.objects.create(tag="test", nsfw=False)

    def test_list_tags(self):
        res = self.client.get("/api/tags/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_tags(self):
        res = self.client.post("/api/tags/", {"tag":"test2","nsfw":True}, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 2)

    def test_detail_tags(self):
        res = self.client.get(f"/api/tags/{self.tag.id}/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["tag"], "test")

    def test_update_tags(self):
        res = self.client.put(f"/api/tags/{self.tag.id}/", {"tag":"nouvtest","nsfw":True}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.tag, "nouvtest")

    def test_delete_tags(self):
        res = self.client.delete(f"/api/tags/{self.tag.id}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)

class TagTestCase(APITestCase):
    def setUp(self):
        self.user = Lecteur.objects.create_user(username="test", password="mdptest", date_naissance=date(2000,1,1))
        self.client.login(username="test", password="mdptest")

        self.tag = Tag.objects.create(tag="test", nsfw=False)

    def test_list_tags(self):
        res = self.client.get("/api/tags/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_tags(self):
        res = self.client.post("/api/tags/", {"tag":"test2","nsfw":True}, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.count(), 2)

    def test_detail_tags(self):
        res = self.client.get(f"/api/tags/{self.tag.id}/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["tag"], "test")

    def test_update_tags(self):
        res = self.client.put(f"/api/tags/{self.tag.id}/", {"tag":"nouvtest","nsfw":True}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.tag, "nouvtest")

    def test_delete_tags(self):
        res = self.client.delete(f"/api/tags/{self.tag.id}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Tag.objects.count(), 0)
