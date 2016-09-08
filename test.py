import unittest.mock
from unittest import TestCase

from corp import work  # your impl file

class BossTest(TestCase):
    def test_profit_adds_up(self):
        worker = unittest.mock.create_autospec(work.Worker)
        worker.work.return_value = 8
        boss = work.Boss(worker)
        self.assertEqual(boss.make_profit(), 8000)
        self.assertEqual(boss.make_profit(), 16000)
        worker.work.return_value = 10
        self.assertEqual(boss.make_profit(), 26000)

        worker.work.assert_has_calls([
            unittest.mock.call(), unittest.mock.call(), unittest.mock.call()
        ])

    @unittest.mock.patch('corp.work.randint', return_value=20)
    def test_profit_adds_up_despite_turnover(self, randint):
        boss = work.Boss(work.Worker())
        self.assertEqual(boss.make_profit(), 20000)
        self.assertEqual(boss.make_profit(), 40000)
        self.assertEqual(boss.make_profit(), 60000)
        self.assertEqual(boss.make_profit(), 80000)

        randint.assert_has_calls([
            unittest.mock.call(1, 40), unittest.mock.call(1, 40),
            unittest.mock.call(1, 40), unittest.mock.call(1, 40)
        ])

    def test_profit_adds_up_despite_strikes(self):
        worker = unittest.mock.create_autospec(work.Worker)
        worker.work.return_value = 12
        boss = work.Boss(worker)

        with unittest.mock.patch('corp.work.Worker') as MockWorker:
            scrub = MockWorker.return_value
            scrub.work.return_value = 4

            self.assertEqual(boss.make_profit(), 12000)
            self.assertEqual(boss.make_profit(), 24000)

            worker.work.side_effect = work.WorkerStrikeException('Faking a strike!')
            self.assertEqual(boss.make_profit(), 28000)
            self.assertEqual(boss.make_profit(), 32000)

            worker.work.assert_has_calls([
                unittest.mock.call(), unittest.mock.call(), unittest.mock.call()
            ])
            scrub.work.assert_has_calls([
                unittest.mock.call(), unittest.mock.call()
            ])

if __name__ == '__main__':
    unittest.main()
