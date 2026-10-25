# -*- coding: utf-8 -*-
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import calcola_dis as dis  # noqa: E402


class TestDis(unittest.TestCase):
    def test_esempio_della_definizione(self):
        # A: 100 posti, 150 presenti; B: 200 posti, 180 presenti; C: 50 posti, 50 presenti
        righe = [
            {"istituto": "A", "cap_reg": 100, "non_disp": 0, "presenti": 150},
            {"istituto": "B", "cap_reg": 200, "non_disp": 30, "presenti": 180},
            {"istituto": "C", "cap_reg": 50, "non_disp": 0, "presenti": 50},
        ]
        a, p, n, t = dis.dis(righe, effettiva=False)
        self.assertEqual((a, n), (150, 1))
        self.assertAlmostEqual(p, 39.5, places=1)
        self.assertAlmostEqual(t, 108.6, places=1)
        a, p, n, t = dis.dis(righe, effettiva=True)
        self.assertEqual((a, n), (330, 2))
        self.assertAlmostEqual(p, 86.8, places=1)

    def test_uguale_alla_capienza_non_conta(self):
        righe = [{"istituto": "C", "cap_reg": 50, "non_disp": 0, "presenti": 50}]
        self.assertEqual(dis.dis(righe)[0], 0)

    def test_capienza_effettiva_non_positiva_esclusa(self):
        righe = [{"istituto": "X", "cap_reg": 10, "non_disp": 10, "presenti": 5}]
        self.assertEqual(dis.dis(righe, effettiva=True)[0], 0)

    def test_file_di_esempio(self):
        percorso = os.path.join(os.path.dirname(__file__), "..", "esempio", "istituti_esempio.csv")
        righe = dis.leggi(percorso)
        self.assertEqual(len(righe), 5)
        self.assertGreater(dis.dis(righe, effettiva=True)[0], dis.dis(righe, effettiva=False)[0])


if __name__ == "__main__":
    unittest.main()
