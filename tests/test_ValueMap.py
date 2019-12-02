import unittest

from ValueMap.ValueMap import ValueMap


class TestValueMap(unittest.TestCase):
    def test_no_parents_get_set(self):
        test_value_map = ValueMap()
        test_value_map["key1"] = "value1"
        self.assertEqual(test_value_map["key1"], "value1")
        with self.assertRaises(KeyError) as context:
            dummy = test_value_map["key2"]
        self.assertTrue("Key key2 is not found" in str(context.exception))

    def test_with_parent_get_set(self):
        parent = ValueMap()
        parent["key1"] = "value1"
        parent["key2"] = "value2"
        self.assertEqual(parent["key1"], "value1")
        self.assertEqual(parent["key2"], "value2")

        child = ValueMap(parent)
        child["key1"] = "childvalue1"
        child["key3"] = "value3"
        self.assertEqual(child["key1"], "childvalue1")
        self.assertEqual(child["key2"], "value2")
        self.assertEqual(child["key3"], "value3")
        self.assertEqual(parent["key1"], "value1")
        self.assertEqual(parent["key2"], "value2")
        with self.assertRaises(KeyError) as context:
            dummy = parent["key3"]
        self.assertTrue("Key key3 is not found" in str(context.exception))


if __name__ == '__main__':
    unittest.main()
