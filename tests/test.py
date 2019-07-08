import requests
import unittest

baseurl='http://127.0.0.1:5000'
class test1(unittest.TestCase):
    def testmain(self):
        res=requests.get(baseurl)
        result=res.json()
        self.assertEqual(result['code'],10200)
    def testusername(self):
        username='test'
        res=requests.get(baseurl+'/user/{}'.format(username))
        result=res.json()
        self.assertEqual(result['message'],'hello, {}'.format(username))
    def testid(self):
        id='1'
        result=requests.get(baseurl+'/id/{}'.format(id)).json()
        self.assertEqual(result['data']['name'],'tom')
        result=requests.get(baseurl+'/id/2').json()
        self.assertEqual(result['message'],'user id null')
        data={'id':123}
        result=requests.post(baseurl+'/id/1',data=data).json()
        self.assertEqual(result['message'],'request method error')

    def testq(self):
        x='selenium'
        result=requests.get(baseurl+'/search/?q={}'.format(x)).json()
        self.assertEqual(result['message'],'success')
        print(result['data'])
    def testlogin(self):
        username='admin'
        password='a123456'
        data={'username':username,'password':password}

        result=requests.post(baseurl+'/login',data=data).json()
        self.assertEqual(result['message'],'login success')



if __name__ == '__main__':
    unittest.main()
