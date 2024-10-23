import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):

    # Part 1

    def test_create_rectangle_1(self):
        point1 = data.Point(2, 2)
        point2 = data.Point(10, 10)
        result = hw2.create_rectangle(point1, point2)
        expected = data.Rectangle(data.Point(2, 10), data.Point(10, 2))
        self.assertEqual(result, expected)

    def test_create_rectangle_2(self):
        point1 = data.Point(7, -2)
        point2 = data.Point(0, -2)
        result = hw2.create_rectangle(point1, point2)
        expected = data.Rectangle(data.Point(0, -2), data.Point(7, -2))
        self.assertEqual(result, expected)

    # Part 2

    def test_shorter_duration_than_1(self):
        duration1 = data.Duration(5, 7)
        duration2 = data.Duration(10, 0)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = True
        self.assertEqual(result, expected)

    def test_shorter_duration_than_2(self):
        duration1 = data.Duration(10, 7)
        duration2 = data.Duration(10, 0)
        result = hw2.shorter_duration_than(duration1, duration2)
        expected = False
        self.assertEqual(result, expected)


    # Part 3

    def test_songs_shorter_than_1(self):
        length = data.Duration(3, 24)
        song1 = data.Song('Artist', 'Title1', data.Duration(3, 21))
        song2 = data.Song('Artist', 'Title2', data.Duration(3, 21))
        song3 = data.Song('Artist', 'Title2', data.Duration(4, 21))
        songs = [song1, song2, song3]
        result = hw2.songs_shorter_than(songs, length)
        expected = [song1, song2]
        self.assertEqual(result, expected)
    
    def test_songs_shorter_than_2(self):
        length = data.Duration(3, 0)
        song1 = data.Song('Artist', 'Title1', data.Duration(3, 0))
        song2 = data.Song('Artist', 'Title2', data.Duration(3, 1))
        song3 = data.Song('Artist', 'Title2', data.Duration(4, 5))
        songs = [song1, song2, song3]
        result = hw2.songs_shorter_than(songs, length)
        expected = []
        self.assertEqual(result, expected)

    def test_songs_shorter_than_3(self):
        length = data.Duration(3, 0)
        songs = []
        result = hw2.songs_shorter_than(songs, length)
        expected = []
        self.assertEqual(result, expected)

    # Part 4

    def test_add_durations_1(self):
        durations = [data.Duration(1, 1), data.Duration(7, 16)]
        result = hw2.add_durations(durations)
        expected = data.Duration(8, 17)
        self.assertEqual(expected, result)

    def test_add_durations_2(self):
        durations = [data.Duration(1, 59), data.Duration(7, 2)]
        result = hw2.add_durations(durations)
        expected = data.Duration(9, 1)
        self.assertEqual(expected, result)

    def test_add_durations_3(self):
        durations = []
        result = hw2.add_durations(durations)
        expected = 0
        self.assertEqual(expected, result)


    def test_running_time_1(self):
        songs = [data.Song("Me", "Me", data.Duration(4, 30)), data.Song("Me", "Me", data.Duration(3, 40))]
        result = hw2.running_time(songs, [0, 1, 0])
        expected = data.Duration(12, 40)
        self.assertEqual(expected, result)

    def test_running_time_2(self):
        songs = []
        result = hw2.running_time(songs, [0])
        expected = 0
        self.assertEqual(expected, result)

    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
