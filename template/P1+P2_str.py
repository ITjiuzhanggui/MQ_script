from template.test_CP import JsonFileXlsx


class C_cells_P(JsonFileXlsx):

    def C_cells_P1(self):
        list_P1_C = []
        for i in range(1, 6):
            list_P1_C.append("C%s" % i)
            list_P1_C.append("C%d" % (i + 6))
            list_P1_C.append("C%d" % (i + 12))
            list_P1_C.append("C%d" % (i + 18))
            list_P1_C.append("C%d" % (i + 24))
            list_P1_C.append("C%d" % (i + 30))
            list_P1_C.append("C%d" % (i + 36))
            list_P1_C.append("C%d" % (i + 42))

        for item in list_P1_C:
            self.worksheet.write_string(item, 'P1/P1', self.cell_format)

    def C_cells_P2(self):
        list_P2_C = []
        for j in range(49, 54):
            list_P2_C.append("C%s" % j)
            list_P2_C.append("C%s" % (j + 6))
            list_P2_C.append("C%s" % (j + 12))
            list_P2_C.append("C%s" % (j + 18))
            list_P2_C.append("C%s" % (j + 24))
            list_P2_C.append("C%s" % (j + 30))
            list_P2_C.append("C%s" % (j + 36))
            list_P2_C.append("C%s" % (j + 42))
            list_P2_C.append("C%s" % (j + 48))
            list_P2_C.append("C%s" % (j + 54))

        for item in list_P2_C:
            self.worksheet.write_string(item, 'P2/P2', self.cell_format)

    def F_cells_P1(self):
        list_P1_F = []
        for i in range(1, 6):
            list_P1_F.append("F%s" % i)
            list_P1_F.append("F%d" % (i + 6))
            list_P1_F.append("F%d" % (i + 12))
            list_P1_F.append("F%d" % (i + 18))
            list_P1_F.append("F%d" % (i + 24))
            list_P1_F.append("F%d" % (i + 30))
            list_P1_F.append("F%d" % (i + 36))
            list_P1_F.append("F%d" % (i + 42))

        for item in list_P1_F:
            self.worksheet.write_string(item, 'P1/P1', self.cell_format)

    def F_cells_P2(self):
        list_P2_F = []
        for j in range(49, 54):
            list_P2_F.append("F%s" % j)
            list_P2_F.append("F%s" % (j + 6))
            list_P2_F.append("F%s" % (j + 12))
            list_P2_F.append("F%s" % (j + 18))
            list_P2_F.append("F%s" % (j + 24))
            list_P2_F.append("F%s" % (j + 30))
            list_P2_F.append("F%s" % (j + 36))
            list_P2_F.append("F%s" % (j + 42))
            list_P2_F.append("F%s" % (j + 48))
            list_P2_F.append("F%s" % (j + 54))

        for item in list_P2_F:
            self.worksheet.write_string(item, 'P2/P2', self.cell_format)


C = C_cells_P(JsonFileXlsx)
C.C_cells_P1()
C.C_cells_P2()
C.F_cells_P1()
C.F_cells_P2()