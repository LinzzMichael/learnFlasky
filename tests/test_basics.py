import unittest

from flask import current_app
from app import create_app, db


class BasicsTestCase(unittest.TestCase):
	#测试前会自动运行
	def setUp(self):
		self.app = create_app('testing')
		self.app_context = self.app.app_context()
		self.app_context.push()
		#创建数据库文件
		db.create_all()

	#测试后自动运行
	def tearDown(self):
		db.session.remove()
		db.drop_all()
		self.app_context.pop()

	def test_app_exist(self):
		self.assertFalse(current_app is None)


	def test_app_is_testing(self):
		self.assertTrue(current_app.config['TESTING'])
