class TestCase():
    def __init__(self, name):
        self.name = name

    def setUp(self):
        self.wasRun=None
        self.wasSetUp = 1

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            exec ("self." + self.name + "()")
        except:
            result.testFailed()
        self.tearDown()
        return result
    
    def tearDown(self):
        pass


class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self,name)

    def setUp(self):
        self.log="setUp "

    def testMethod(self):
        self.wasRun=1
        self.log += "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception
   

class TestCaseTest(TestCase):
    
    def testTemplateMethod(self):
        test  = WasRun("testMethod")
        test.run()
        assert("setUp testMethod tearDown " == test.log)

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert ("1 run, 0 failed" == result.summary())

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        print '--'
        print result.summary()
        assert ('1 run, 1 failed' == result.summary())

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert ('1 run, 1 failed' == result.summary())

class TestResult():
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.errorCount += 1

    def summary(self):
        return '%d run, %d failed' %(self.runCount, self.errorCount)

print TestCaseTest("testTemplateMethod").run().summary()
print TestCaseTest("testResult").run().summary()
print TestCaseTest("testFailedResult").run().summary()
print TestCaseTest("testFailedResultFormating").run().summary()
        
