from template.test_CP import JsonFileXlsx


class Merget(JsonFileXlsx):

    def Merget_cell(self):
        # 合并单元格---P1
        self.get_merge_range('A1:A5', 'OLINUX-5025', self.cell_format)
        self.get_merge_range('B1:B5', 'ST_PERF_Single_80_geometry_APL_I', self.cell_format)

        self.get_merge_range('A7:A11', 'OLINUX-5026', self.cell_format)
        self.get_merge_range('B7:B11', 'ST_PERF_Single_30_geometry_APL_I', self.cell_format)

        self.get_merge_range('A13:A17', 'OLINUX-5028', self.cell_format)
        self.get_merge_range('B13:B17', 'ST_PERF_Multi_80_geometry_APL_I', self.cell_format)

        self.get_merge_range('A19:A23', 'OLINUX-5031', self.cell_format)
        self.get_merge_range('B19:B23', 'ST_PERF_Tex_80_APL_I', self.cell_format)

        self.get_merge_range('A25:A29', 'OLINUX-5032', self.cell_format)
        self.get_merge_range('B25:B29', 'ST_PERF_Long_80_APL_I', self.cell_format)

        self.get_merge_range('A31:A35', 'OLINUX-5046', self.cell_format)
        self.get_merge_range('B31:B35', 'ST_PERF_Single_80_shader_APL_I', self.cell_format)

        self.get_merge_range('A37:A41', 'OLINUX-5047', self.cell_format)
        self.get_merge_range('B37:B41', 'ST_PERF_Multi_80_shader_APL_I', self.cell_format)

        self.get_merge_range('A43:A47', 'OLINUX-5048', self.cell_format)
        self.get_merge_range('B43:B47', 'ST_PERF_Tex_flat_APL_I', self.cell_format)

        # 合并单元格---P2
        self.get_merge_range('A49:A53', 'OLINUX-5036', self.cell_format)
        self.get_merge_range('B49:B53', 'ST_PERF_Long_80_APL_I_fps', self.cell_format)

        self.get_merge_range('A55:A59', 'OLINUX-5037', self.cell_format)
        self.get_merge_range('B55:B59', 'ST_PERF_Multi_30_geometry_APL_I_fps', self.cell_format)

        self.get_merge_range('A61:A65', 'OLINUX-5038', self.cell_format)
        self.get_merge_range('B61:B65', 'ST_PERF_Multi_30_shader_APL_I_fps', self.cell_format)

        self.get_merge_range('A67:A71', 'OLINUX-5039', self.cell_format)
        self.get_merge_range('B67:B71', 'ST_PERF_Multi_80_geometry_APL_I_fps', self.cell_format)

        self.get_merge_range('A73:A77', 'OLINUX-5040', self.cell_format)
        self.get_merge_range('B73:B77', 'ST_PERF_Multi_80_shader_APL_I_fps', self.cell_format)

        self.get_merge_range('A79:A83', 'OLINUX-5041', self.cell_format)
        self.get_merge_range('B79:B83', 'ST_PERF_Single_30_geometry_APL_I_fps', self.cell_format)

        self.get_merge_range('A85:A89', 'OLINUX-5042', self.cell_format)
        self.get_merge_range('B85:B89', 'ST_PERF_Single_30_shader_APL_I_fps', self.cell_format)

        self.get_merge_range('A91:A95', 'OLINUX-5043', self.cell_format)
        self.get_merge_range('B91:B95', 'ST_PERF_Single_80_geometry_APL_I_fps', self.cell_format)

        self.get_merge_range('A97:A101', 'OLINUX-5044', self.cell_format)
        self.get_merge_range('B97:B101', 'ST_PERF_Single_80_shader_APL_I_fps', self.cell_format)

        self.get_merge_range('A103:A107', 'OLINUX-5045', self.cell_format)
        self.get_merge_range('B103:B107', 'ST_PERF_Tex_80_APL_I_fps', self.cell_format)

        # 合并单元格4998-4999
        self.get_merge_range(
            'A109:D188',
            'Per Domain Graphics & Media Prioritization (multiple domains) [APL-I]  5%(-)' + '\n' +
            'Per Domain Graphics & Media SLA with QoS (multiple domains) [APL-I] - QoS in SOS  80%(+)' + '\n' +
            'Per Domain Graphics & Media SLA with QoS (multiple domains) [APL-I] - QoS in UOS  90%(+)' + '\n',
            self.cell_2_format)

        # 4998-4999 F列
        self.get_merge_range('F109:I123', '', self.cell_2_format)
        self.get_merge_range('E109:E123', None, self.cell_5_format)
        self.get_merge_range('E124:N124', None, self.cell_3_format)

        self.get_merge_range('F125:I139', '', self.cell_2_format)
        self.get_merge_range('E125:E139', None, self.cell_5_format)
        self.get_merge_range('E140:N140', None, self.cell_3_format)

        self.get_merge_range('F141:I155', '', self.cell_2_format)
        self.get_merge_range('E141:E155', None, self.cell_5_format)
        self.get_merge_range('E156:N156', None, self.cell_3_format)

        self.get_merge_range('F157:I171', '', self.cell_2_format)
        self.get_merge_range('E157:E171', None, self.cell_5_format)
        self.get_merge_range('E172:N172', None, self.cell_3_format)

        self.get_merge_range('F173:I187', '', self.cell_2_format)
        self.get_merge_range('E173:E187', None, self.cell_5_format)
        self.get_merge_range('E188:N188', None, self.cell_3_format)

        # 4998-4999 N列
        self.get_merge_range('K109:N123', '', self.cell_2_format)
        self.get_merge_range('J109:J123', '', self.cell_5_format)

        self.get_merge_range('K125:N139', '', self.cell_2_format)
        self.get_merge_range('J125:J139', '', self.cell_5_format)

        self.get_merge_range('K141:N155', '', self.cell_2_format)
        self.get_merge_range('J141:J155', '', self.cell_5_format)

        self.get_merge_range('K157:N171', '', self.cell_2_format)
        self.get_merge_range('J157:J171', '', self.cell_5_format)

        self.get_merge_range('K173:N187', '', self.cell_2_format)
        self.get_merge_range('J173:J187', '', self.cell_5_format)


M = Merget(JsonFileXlsx)
M.Merget_cell()