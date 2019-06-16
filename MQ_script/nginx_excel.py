import pandas as pd
from openpyxl import load_workbook
pd.set_option("expand_frame_repr", False)


# def calc_rate(default_nginx_list, clear_nginx_list):
#     rate_list = []
#     if len(default_nginx_list) != len(clear_nginx_list):
#         print("nginx:data error")
#         return None
#
#     tmp_result_list = []
#     for i in range(len(default_nginx_list)):
#         print(clear_nginx_list[i], 6 * "-", default_nginx_list[i])
#         tmp_ret = float(clear_nginx_list[i] / float(default_nginx_list[i]))
#         print(tmp_ret)
#         result = 1 / tmp_ret - 1
#         tmp_result_list.append(result)
#
#     for i in range(len(tmp_result_list)):
#         ret = tmp_result_list[i]
#         ret = str(ret * 100)[:4] + "%"
#         rate_list.append(ret)
#     return rate_list
def read_log(file_name):
    with open(file_name, "r", encoding="utf-8")as f:
        return f.read()


def read_status_logs(status_log):
    with open(status_log, "r", encoding="utf-8")as f:
        return f.read()


def NginxExcel():
    clearlinux_version_dict = df_json.loc["clearlinux_version"].loc["status_Clr"]
    clearlinux_version = clearlinux_version_dict["clear_linux"]

    default_dict = df_json.loc["nginx"].loc["default"]
    clear_dict = df_json.loc["nginx"].loc["clear"]
    status_def_dict = df_json.loc["nginx"].loc["status_def"]
    status_clr_dict = df_json.loc["nginx"].loc["status_Clr"]

    x_test = ["Time taken for tests",
              "Time per request",
              "Time per request(all)",
              "Requests per second",
              "Transfer rate",
              ]

    x_status = ["Total",
                "Base_Layer",
                "MicroService_layer",
                ]

    test_col = pd.Series(x_test)
    # print("test_col+++%s" % test_col)
    status_col = pd.Series(x_status)
    # print("status_col===%s" % status_col)
    default_nginx_list = [default_dict["Time taken for tests"], default_dict["Time per request"],
                          default_dict["Time per request(all)"], default_dict["Requests per second"],
                          default_dict["Transfer rate"]]

    # print("default_nginx_list===%s" % default_nginx_list)
    default_col = pd.Series(default_nginx_list)

    clear_nginx_list = [clear_dict["Time taken for tests"], clear_dict["Time per request"],
                        clear_dict["Time per request(all)"], clear_dict["Requests per second"],
                        clear_dict["Transfer rate"]]
    # print("clear_nginx_list----%s" % clear_nginx_list)
    # rate_col = calc_rate(default_nginx_list, clear_nginx_list)
    clear_col = pd.Series(clear_nginx_list)

    status_def_list = [status_def_dict["Total"], status_def_dict["Base_Layer"],
                       status_def_dict["MicroService_layer"]]
    status_def_col = pd.Series(status_def_list)

    status_clr_list = [status_clr_dict["Total"], status_clr_dict["Base_Layer"],
                       status_clr_dict["MicroService_layer"]]
    status_clr_col = pd.Series(status_clr_list)

    data_frame = {"Performance": status_col, "Default docker": status_def_col, "Clear docker": status_clr_col}
    data_frame2 = {"Performance": test_col, "Default docker": default_col,
                   "Clear docker": clear_col, }  # "Rate": rate_col}

    df_excel = pd.DataFrame(data_frame)
    df_excel2 = pd.DataFrame(data_frame2)

    # writer = pd.ExcelWriter(r"C:\Users\xinhuizx\python_Code\MQ_scr\MQ_tset.xlsx")
    df_excel2.to_excel(writer, sheet_name="nginx", index=False, startrow=9)
    df_excel.to_excel(writer, sheet_name="nginx", index=False, startrow=0)
    writer.save()
    print("Successfully Nginx!!!")


def Httpd():
    default_dict = df_json.loc["httpd"].loc["default"]
    # print(default_dict)
    clear_dict = df_json.loc["httpd"].loc["clear"]
    status_def_dict = df_json.loc["httpd"].loc["status_def"]
    status_clr_dict = df_json.loc["httpd"].loc["status_Clr"]
    clearlinux_version_dict = df_json.loc["clearlinux_version"].loc["status_Clr"]
    clearlinux_version = clearlinux_version_dict["clear_linux"]

    x_test = ["Time taken for tests",
              "Time per request",
              "Time per request(all)",
              "Requests per second",
              "Transfer rate"]

    x_status = ["Total",
                "Base_Layer",
                "MicroService_layer",
                ]

    test_col = pd.Series(x_test)
    status_col = pd.Series(x_status)

    default_httpd_list = [default_dict["Time taken for tests"],
                          default_dict["Time per request"],
                          default_dict["Time per request(all)"],
                          default_dict["Requests per second"],
                          default_dict["Transfer rate"]
                          ]

    default_col = pd.Series(default_httpd_list)

    clear_httpd_list = [clear_dict["Time taken for tests"],
                        clear_dict["Time per request"],
                        clear_dict["Time per request(all)"],
                        clear_dict["Requests per second"],
                        clear_dict["Transfer rate"]
                        ]

    clear_col = pd.Series(clear_httpd_list)

    status_def_list = [status_def_dict["Total"],
                       status_def_dict["Base_Layer"],
                       status_def_dict["MicroService_layer"]
                       ]

    status_def_col = pd.Series(status_def_list)

    status_clr_list = [status_clr_dict["Total"],
                       status_clr_dict["Base_Layer"],
                       status_clr_dict["MicroService_layer"]
                       ]

    status_clr_col = pd.Series(status_clr_list)

    data_frame_status = {"Performance": status_col, "Default docker": status_def_col, "clear docker": status_clr_col}
    data_frame_test = {"Performance": test_col, "Default docker": default_col, "clear docker": clear_col}

    df_exce_status = pd.DataFrame(data_frame_status)
    df_exce_test = pd.DataFrame(data_frame_test)

    df_exce_status.to_excel(writer, sheet_name="httpd", index=False, startrow=0)
    df_exce_test.to_excel(writer, sheet_name="httpd", index=False, startrow=9)
    writer.save()
    print("Successfully Httpd!!!")


if __name__ == '__main__':
    df_json = pd.read_json(r"C:\Users\xinhuizx\python_Code\MQ_script\data_LOG.json")

    writer = pd.ExcelWriter(r"C:\Users\xinhuizx\python_Code\MQ_script\MQ_tset.xlsx")

    NginxExcel()
    Httpd()
