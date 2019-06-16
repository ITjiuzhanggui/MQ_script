import os

import pandas as pd

pd.set_option("expand_frame_repr", False)


def read_log(file_name):
    with open(file_name, "r", encoding="utf-8")as f:
        return f.read()


#
# def read_status_logs(status_log):
#     with open(status_log, "r", encoding="utf-8")as f:
#         return f.read()


def read_status_log(status_json_filename):
    df_json = pd.read_json(status_json_filename)
    status_def_dict = df_json.loc["ruby"].loc["status_def"]
    status_clr_dict = df_json.loc["ruby"].loc["status_Clr"]
    clearlinux_version_dict = df_json.loc["clearlinux_version"].loc["status_Clr"]
    clearlinux_version = clearlinux_version_dict["clear_linux"]

    x_status = ["Total",
                "Base_Layer",
                "MicroService_layer",
                ]

    status_col = pd.Series(x_status)

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
    df_exce_status = pd.DataFrame(data_frame_status)
    df_exce_status.to_excel(writer, sheet_name="ruby", index=False, startrow=0)
    # df_exce_test.to_excel(excel_file, sheet_name="ruby", index=False, startrow=9)
    writer.save()
    # print("Successfully Httpd!!!")


def httpd():
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


def Ruby(writer, df_json, loop_count):
    # print(df_json.loc["ruby"])
    default_dict = df_json.loc["ruby"].loc["default"]
    # print(default_dict)
    clear_dict = df_json.loc["ruby"].loc["clear"]

    x_test = ["app_answer",
              "app_answer",
              "app_erb",
              "app_factorial",
              "app_fib",
              "app_lc_fizzbuzz",
              "app_mandelbrot",
              "app_pentomino",
              "app_raise",
              "app_strconcat",
              "app_tak",
              "app_tarai",
              "app_uri",
              "array_sample_100k_10",
              "array_sample_100k_11",
              "array_sample_100k__100",
              "array_sample_100k__1k",
              "array_sample_100k__6k",
              "array_sample_100k___10k",
              "array_sample_100k___50k",
              "array_shift",
              "array_small_and",
              "array_small_diff",
              "array_small_or",
              "array_sort_block",
              "array_sort_float",
              "array_values_at_int",
              "array_values_at_range",
              "bighash",
              "complex_float_add",
              "complex_float_div",
              "complex_float_mul",
              "complex_float_new",
              "complex_float_power",
              "complex_float_sub",
              "dir_empty_p",
              "enum_lazy_grep_v_100",
              "enum_lazy_grep_v_20",
              "enum_lazy_grep_v_50",
              "enum_lazy_uniq_100",
              "enum_lazy_uniq_20",
              "enum_lazy_uniq_50",
              "erb_render",
              "fiber_chain",
              "file_chmod",
              "file_rename",
              "hash_aref_dsym",
              "hash_aref_dsym_long",
              "hash_aref_fix",
              "hash_aref_flo",
              "hash_aref_miss",
              "hash_aref_str",
              "hash_aref_sym",
              "hash_aref_sym_long",
              "hash_flatten",
              "hash_ident_flo",
              "hash_ident_num",
              "hash_ident_obj",
              "hash_ident_str",
              "hash_ident_sym",
              "hash_keys",
              "hash_literal_small2",
              "hash_literal_small4",
              "hash_literal_small8",
              "hash_long",
              "hash_shift",
              "hash_shift_u16",
              "hash_shift_u24",
              "hash_shift_u32",
              "hash_small2",
              "hash_small4",
              "hash_small8",
              "hash_to_proc",
              "hash_values",
              "int_quo",
              "io_copy_stream_write",
              "io_copy_stream_write_socket",
              "io_file_create",
              "io_file_read",
              "io_file_write",
              "io_nonblock_noex",
              "io_nonblock_noex2",
              "io_pipe_rw",
              "io_select",
              "io_select2",
              "io_select3",
              "loop_for",
              "loop_generator",
              "loop_times",
              "loop_whileloop",
              "loop_whileloop2",
              "marshal_dump_flo",
              "marshal_dump_load_geniv",
              "marshal_dump_load_time",
              "require",
              "require_thread",
              "securerandom",
              "so_ackermann",
              "so_array",
              "so_binary_trees",
              "so_concatenate",
              "so_count_words",
              "so_exception",
              "so_fannkuch",
              "so_fasta",
              "so_k_nucleotidepreparing",
              "so_lists",
              "so_mandelbrot",
              "so_matrix",
              "so_meteor_contest",
              "so_nbody",
              "so_nested_loop",
              "so_nsieve",
              "so_nsieve_bits",
              "so_object",
              "so_partial_sums",
              "so_pidigits",
              "so_random",
              "so_reverse_complementpreparing",
              "so_sieve",
              "so_spectralnorm",
              "string_index",
              "string_scan_re",
              "string_scan_str",
              "time_subsec",
              "vm1_attr_ivar",
              "vm1_attr_ivar_set",
              "vm1_block",
              "vm1_blockparam",
              "vm1_blockparam_call",
              "vm1_blockparam_pass",
              "vm1_blockparam_yield",
              "vm1_const",
              "vm1_ensure",
              "vm1_float_simple",
              "vm1_gc_short_lived",
              "vm1_gc_short_with_complex_long",
              "vm1_gc_short_with_long",
              "vm1_gc_short_with_symbol",
              "vm1_gc_wb_ary",
              "vm1_gc_wb_ary_promoted",
              "vm1_gc_wb_obj",
              "vm1_gc_wb_obj_promoted",
              "vm1_ivar",
              "vm1_ivar_set",
              "vm1_length",
              "vm1_lvar_init",
              "vm1_lvar_set",
              "vm1_neq",
              "vm1_not",
              "vm1_rescue",
              "vm1_simplereturn",
              "vm1_swap",
              "vm1_yield",
              "vm2_array",
              "vm2_bigarray",
              "vm2_bighash",
              "vm2_case",
              "vm2_case_lit",
              "vm2_defined_method",
              "vm2_dstr",
              "vm2_eval",
              "vm2_fiber_switch",
              "vm2_freezestring",
              "vm2_method",
              "vm2_method_missing",
              "vm2_method_with_block",
              "vm2_module_ann_const_set",
              "vm2_module_const_set",
              "vm2_mutex",
              "vm2_newlambda",
              "vm2_poly_method",
              "vm2_poly_method_ov",
              "vm2_poly_singleton",
              "vm2_proc",
              "vm2_raise1",
              "vm2_raise2",
              "vm2_regexp",
              "vm2_send",
              "vm2_string_literal",
              "vm2_struct_big_aref_hi",
              "vm2_struct_big_aref_lo",
              "vm2_struct_big_aset",
              "vm2_struct_big_href_hi",
              "vm2_struct_big_href_lo",
              "vm2_struct_big_hset",
              "vm2_struct_small_aref",
              "vm2_struct_small_aset",
              "vm2_struct_small_href",
              "vm2_struct_small_hset",
              "vm2_super",
              "vm2_unif1",
              "vm2_zsuper",
              "vm3_backtrace",
              "vm3_clearmethodcache",
              "vm3_gc",
              "vm3_gc_old_full",
              "vm3_gc_old_immediate",
              "vm3_gc_old_lazy",
              "vm_symbol_block_pass",
              "vm_thread_alive_check1",
              "vm_thread_close",
              "vm_thread_condvar1",
              "vm_thread_condvar2",
              "vm_thread_create_join",
              "vm_thread_mutex1",
              "vm_thread_mutex2",
              "vm_thread_mutex3",
              "vm_thread_pass",
              "vm_thread_pass_flood",
              "vm_thread_pipe",
              "vm_thread_queue",
              "vm_thread_sized_queue",
              "vm_thread_sized_queue2",
              "vm_thread_sized_queue3",
              "vm_thread_sized_queue4"

              ]

    test_col = pd.Series(x_test)

    default_ruby_list = [default_dict["app_answer"],
                         default_dict["app_answer"],
                         default_dict["app_erb"],
                         default_dict["app_factorial"],
                         default_dict["app_fib"],
                         default_dict["app_lc_fizzbuzz"],
                         default_dict["app_mandelbrot"],
                         default_dict["app_pentomino"],
                         default_dict["app_raise"],
                         default_dict["app_strconcat"],
                         default_dict["app_tak"],
                         default_dict["app_tarai"],
                         default_dict["app_uri"],
                         default_dict["array_sample_100k_10"],
                         default_dict["array_sample_100k_11"],
                         default_dict["array_sample_100k__100"],
                         default_dict["array_sample_100k__1k"],
                         default_dict["array_sample_100k__6k"],
                         default_dict["array_sample_100k___10k"],
                         default_dict["array_sample_100k___50k"],
                         default_dict["array_shift"],
                         default_dict["array_small_and"],
                         default_dict["array_small_diff"],
                         default_dict["array_small_or"],
                         default_dict["array_sort_block"],
                         default_dict["array_sort_float"],
                         default_dict["array_values_at_int"],
                         default_dict["array_values_at_range"],
                         default_dict["bighash"],
                         default_dict["complex_float_add"],
                         default_dict["complex_float_div"],
                         default_dict["complex_float_mul"],
                         default_dict["complex_float_new"],
                         default_dict["complex_float_power"],
                         default_dict["complex_float_sub"],
                         default_dict["dir_empty_p"],
                         default_dict["enum_lazy_grep_v_100"],
                         default_dict["enum_lazy_grep_v_20"],
                         default_dict["enum_lazy_grep_v_50"],
                         default_dict["enum_lazy_uniq_100"],
                         default_dict["enum_lazy_uniq_20"],
                         default_dict["enum_lazy_uniq_50"],
                         default_dict["erb_render"],
                         default_dict["fiber_chain"],
                         default_dict["file_chmod"],
                         default_dict["file_rename"],
                         default_dict["hash_aref_dsym"],
                         default_dict["hash_aref_dsym_long"],
                         default_dict["hash_aref_fix"],
                         default_dict["hash_aref_flo"],
                         default_dict["hash_aref_miss"],
                         default_dict["hash_aref_str"],
                         default_dict["hash_aref_sym"],
                         default_dict["hash_aref_sym_long"],
                         default_dict["hash_flatten"],
                         default_dict["hash_ident_flo"],
                         default_dict["hash_ident_num"],
                         default_dict["hash_ident_obj"],
                         default_dict["hash_ident_str"],
                         default_dict["hash_ident_sym"],
                         default_dict["hash_keys"],
                         default_dict["hash_literal_small2"],
                         default_dict["hash_literal_small4"],
                         default_dict["hash_literal_small8"],
                         default_dict["hash_long"],
                         default_dict["hash_shift"],
                         default_dict["hash_shift_u16"],
                         default_dict["hash_shift_u24"],
                         default_dict["hash_shift_u32"],
                         default_dict["hash_small2"],
                         default_dict["hash_small4"],
                         default_dict["hash_small8"],
                         default_dict["hash_to_proc"],
                         default_dict["hash_values"],
                         default_dict["int_quo"],
                         default_dict["io_copy_stream_write"],
                         default_dict["io_copy_stream_write_socket"],
                         default_dict["io_file_create"],
                         default_dict["io_file_read"],
                         default_dict["io_file_write"],
                         default_dict["io_nonblock_noex"],
                         default_dict["io_nonblock_noex2"],
                         default_dict["io_pipe_rw"],
                         default_dict["io_select"],
                         default_dict["io_select2"],
                         default_dict["io_select3"],
                         default_dict["loop_for"],
                         default_dict["loop_generator"],
                         default_dict["loop_times"],
                         default_dict["loop_whileloop"],
                         default_dict["loop_whileloop2"],
                         default_dict["marshal_dump_flo"],
                         default_dict["marshal_dump_load_geniv"],
                         default_dict["marshal_dump_load_time"],
                         default_dict["require"],
                         default_dict["require_thread"],
                         default_dict["securerandom"],
                         default_dict["so_ackermann"],
                         default_dict["so_array"],
                         default_dict["so_binary_trees"],
                         default_dict["so_concatenate"],
                         default_dict["so_count_words"],
                         default_dict["so_exception"],
                         default_dict["so_fannkuch"],
                         default_dict["so_fasta"],
                         default_dict["so_k_nucleotidepreparing"],
                         default_dict["so_lists"],
                         default_dict["so_mandelbrot"],
                         default_dict["so_matrix"],
                         default_dict["so_meteor_contest"],
                         default_dict["so_nbody"],
                         default_dict["so_nested_loop"],
                         default_dict["so_nsieve"],
                         default_dict["so_nsieve_bits"],
                         default_dict["so_object"],
                         default_dict["so_partial_sums"],
                         default_dict["so_pidigits"],
                         default_dict["so_random"],
                         default_dict["so_reverse_complementpreparing"],
                         default_dict["so_sieve"],
                         default_dict["so_spectralnorm"],
                         default_dict["string_index"],
                         default_dict["string_scan_re"],
                         default_dict["string_scan_str"],
                         default_dict["time_subsec"],
                         default_dict["vm1_attr_ivar"],
                         default_dict["vm1_attr_ivar_set"],
                         default_dict["vm1_block"],
                         default_dict["vm1_blockparam"],
                         default_dict["vm1_blockparam_call"],
                         default_dict["vm1_blockparam_pass"],
                         default_dict["vm1_blockparam_yield"],
                         default_dict["vm1_const"],
                         default_dict["vm1_ensure"],
                         default_dict["vm1_float_simple"],
                         default_dict["vm1_gc_short_lived"],
                         default_dict["vm1_gc_short_with_complex_long"],
                         default_dict["vm1_gc_short_with_long"],
                         default_dict["vm1_gc_short_with_symbol"],
                         default_dict["vm1_gc_wb_ary"],
                         default_dict["vm1_gc_wb_ary_promoted"],
                         default_dict["vm1_gc_wb_obj"],
                         default_dict["vm1_gc_wb_obj_promoted"],
                         default_dict["vm1_ivar"],
                         default_dict["vm1_ivar_set"],
                         default_dict["vm1_length"],
                         default_dict["vm1_lvar_init"],
                         default_dict["vm1_lvar_set"],
                         default_dict["vm1_neq"],
                         default_dict["vm1_not"],
                         default_dict["vm1_rescue"],
                         default_dict["vm1_simplereturn"],
                         default_dict["vm1_swap"],
                         default_dict["vm1_yield"],
                         default_dict["vm2_array"],
                         default_dict["vm2_bigarray"],
                         default_dict["vm2_bighash"],
                         default_dict["vm2_case"],
                         default_dict["vm2_case_lit"],
                         default_dict["vm2_defined_method"],
                         default_dict["vm2_dstr"],
                         default_dict["vm2_eval"],
                         default_dict["vm2_fiber_switch"],
                         default_dict["vm2_freezestring"],
                         default_dict["vm2_method"],
                         default_dict["vm2_method_missing"],
                         default_dict["vm2_method_with_block"],
                         default_dict["vm2_module_ann_const_set"],
                         default_dict["vm2_module_const_set"],
                         default_dict["vm2_mutex"],
                         default_dict["vm2_newlambda"],
                         default_dict["vm2_poly_method"],
                         default_dict["vm2_poly_method_ov"],
                         default_dict["vm2_poly_singleton"],
                         default_dict["vm2_proc"],
                         default_dict["vm2_raise1"],
                         default_dict["vm2_raise2"],
                         default_dict["vm2_regexp"],
                         default_dict["vm2_send"],
                         default_dict["vm2_string_literal"],
                         default_dict["vm2_struct_big_aref_hi"],
                         default_dict["vm2_struct_big_aref_lo"],
                         default_dict["vm2_struct_big_aset"],
                         default_dict["vm2_struct_big_href_hi"],
                         default_dict["vm2_struct_big_href_lo"],
                         default_dict["vm2_struct_big_hset"],
                         default_dict["vm2_struct_small_aref"],
                         default_dict["vm2_struct_small_aset"],
                         default_dict["vm2_struct_small_href"],
                         default_dict["vm2_struct_small_hset"],
                         default_dict["vm2_super"],
                         default_dict["vm2_unif1"],
                         default_dict["vm2_zsuper"],
                         default_dict["vm3_backtrace"],
                         default_dict["vm3_clearmethodcache"],
                         default_dict["vm3_gc"],
                         default_dict["vm3_gc_old_full"],
                         default_dict["vm3_gc_old_immediate"],
                         default_dict["vm3_gc_old_lazy"],
                         default_dict["vm_symbol_block_pass"],
                         default_dict["vm_thread_alive_check1"],
                         default_dict["vm_thread_close"],
                         default_dict["vm_thread_condvar1"],
                         default_dict["vm_thread_condvar2"],
                         default_dict["vm_thread_create_join"],
                         default_dict["vm_thread_mutex1"],
                         default_dict["vm_thread_mutex2"],
                         default_dict["vm_thread_mutex3"],
                         default_dict["vm_thread_pass"],
                         default_dict["vm_thread_pass_flood"],
                         default_dict["vm_thread_pipe"],
                         default_dict["vm_thread_queue"],
                         default_dict["vm_thread_sized_queue"],
                         default_dict["vm_thread_sized_queue2"],
                         default_dict["vm_thread_sized_queue3"],
                         default_dict["vm_thread_sized_queue4"]
                         ]

    default_col = pd.Series(default_ruby_list)

    clear_ruby_list = [default_dict["app_answer"],
                       default_dict["app_answer"],
                       default_dict["app_erb"],
                       default_dict["app_factorial"],
                       default_dict["app_fib"],
                       default_dict["app_lc_fizzbuzz"],
                       default_dict["app_mandelbrot"],
                       default_dict["app_pentomino"],
                       default_dict["app_raise"],
                       default_dict["app_strconcat"],
                       default_dict["app_tak"],
                       default_dict["app_tarai"],
                       default_dict["app_uri"],
                       default_dict["array_sample_100k_10"],
                       default_dict["array_sample_100k_11"],
                       default_dict["array_sample_100k__100"],
                       default_dict["array_sample_100k__1k"],
                       default_dict["array_sample_100k__6k"],
                       default_dict["array_sample_100k___10k"],
                       default_dict["array_sample_100k___50k"],
                       default_dict["array_shift"],
                       default_dict["array_small_and"],
                       default_dict["array_small_diff"],
                       default_dict["array_small_or"],
                       default_dict["array_sort_block"],
                       default_dict["array_sort_float"],
                       default_dict["array_values_at_int"],
                       default_dict["array_values_at_range"],
                       default_dict["bighash"],
                       default_dict["complex_float_add"],
                       default_dict["complex_float_div"],
                       default_dict["complex_float_mul"],
                       default_dict["complex_float_new"],
                       default_dict["complex_float_power"],
                       default_dict["complex_float_sub"],
                       default_dict["dir_empty_p"],
                       default_dict["enum_lazy_grep_v_100"],
                       default_dict["enum_lazy_grep_v_20"],
                       default_dict["enum_lazy_grep_v_50"],
                       default_dict["enum_lazy_uniq_100"],
                       default_dict["enum_lazy_uniq_20"],
                       default_dict["enum_lazy_uniq_50"],
                       default_dict["erb_render"],
                       default_dict["fiber_chain"],
                       default_dict["file_chmod"],
                       default_dict["file_rename"],
                       default_dict["hash_aref_dsym"],
                       default_dict["hash_aref_dsym_long"],
                       default_dict["hash_aref_fix"],
                       default_dict["hash_aref_flo"],
                       default_dict["hash_aref_miss"],
                       default_dict["hash_aref_str"],
                       default_dict["hash_aref_sym"],
                       default_dict["hash_aref_sym_long"],
                       default_dict["hash_flatten"],
                       default_dict["hash_ident_flo"],
                       default_dict["hash_ident_num"],
                       default_dict["hash_ident_obj"],
                       default_dict["hash_ident_str"],
                       default_dict["hash_ident_sym"],
                       default_dict["hash_keys"],
                       default_dict["hash_literal_small2"],
                       default_dict["hash_literal_small4"],
                       default_dict["hash_literal_small8"],
                       default_dict["hash_long"],
                       default_dict["hash_shift"],
                       default_dict["hash_shift_u16"],
                       default_dict["hash_shift_u24"],
                       default_dict["hash_shift_u32"],
                       default_dict["hash_small2"],
                       default_dict["hash_small4"],
                       default_dict["hash_small8"],
                       default_dict["hash_to_proc"],
                       default_dict["hash_values"],
                       default_dict["int_quo"],
                       default_dict["io_copy_stream_write"],
                       default_dict["io_copy_stream_write_socket"],
                       default_dict["io_file_create"],
                       default_dict["io_file_read"],
                       default_dict["io_file_write"],
                       default_dict["io_nonblock_noex"],
                       default_dict["io_nonblock_noex2"],
                       default_dict["io_pipe_rw"],
                       default_dict["io_select"],
                       default_dict["io_select2"],
                       default_dict["io_select3"],
                       default_dict["loop_for"],
                       default_dict["loop_generator"],
                       default_dict["loop_times"],
                       default_dict["loop_whileloop"],
                       default_dict["loop_whileloop2"],
                       default_dict["marshal_dump_flo"],
                       default_dict["marshal_dump_load_geniv"],
                       default_dict["marshal_dump_load_time"],
                       default_dict["require"],
                       default_dict["require_thread"],
                       default_dict["securerandom"],
                       default_dict["so_ackermann"],
                       default_dict["so_array"],
                       default_dict["so_binary_trees"],
                       default_dict["so_concatenate"],
                       default_dict["so_count_words"],
                       default_dict["so_exception"],
                       default_dict["so_fannkuch"],
                       default_dict["so_fasta"],
                       default_dict["so_k_nucleotidepreparing"],
                       default_dict["so_lists"],
                       default_dict["so_mandelbrot"],
                       default_dict["so_matrix"],
                       default_dict["so_meteor_contest"],
                       default_dict["so_nbody"],
                       default_dict["so_nested_loop"],
                       default_dict["so_nsieve"],
                       default_dict["so_nsieve_bits"],
                       default_dict["so_object"],
                       default_dict["so_partial_sums"],
                       default_dict["so_pidigits"],
                       default_dict["so_random"],
                       default_dict["so_reverse_complementpreparing"],
                       default_dict["so_sieve"],
                       default_dict["so_spectralnorm"],
                       default_dict["string_index"],
                       default_dict["string_scan_re"],
                       default_dict["string_scan_str"],
                       default_dict["time_subsec"],
                       default_dict["vm1_attr_ivar"],
                       default_dict["vm1_attr_ivar_set"],
                       default_dict["vm1_block"],
                       default_dict["vm1_blockparam"],
                       default_dict["vm1_blockparam_call"],
                       default_dict["vm1_blockparam_pass"],
                       default_dict["vm1_blockparam_yield"],
                       default_dict["vm1_const"],
                       default_dict["vm1_ensure"],
                       default_dict["vm1_float_simple"],
                       default_dict["vm1_gc_short_lived"],
                       default_dict["vm1_gc_short_with_complex_long"],
                       default_dict["vm1_gc_short_with_long"],
                       default_dict["vm1_gc_short_with_symbol"],
                       default_dict["vm1_gc_wb_ary"],
                       default_dict["vm1_gc_wb_ary_promoted"],
                       default_dict["vm1_gc_wb_obj"],
                       default_dict["vm1_gc_wb_obj_promoted"],
                       default_dict["vm1_ivar"],
                       default_dict["vm1_ivar_set"],
                       default_dict["vm1_length"],
                       default_dict["vm1_lvar_init"],
                       default_dict["vm1_lvar_set"],
                       default_dict["vm1_neq"],
                       default_dict["vm1_not"],
                       default_dict["vm1_rescue"],
                       default_dict["vm1_simplereturn"],
                       default_dict["vm1_swap"],
                       default_dict["vm1_yield"],
                       default_dict["vm2_array"],
                       default_dict["vm2_bigarray"],
                       default_dict["vm2_bighash"],
                       default_dict["vm2_case"],
                       default_dict["vm2_case_lit"],
                       default_dict["vm2_defined_method"],
                       default_dict["vm2_dstr"],
                       default_dict["vm2_eval"],
                       default_dict["vm2_fiber_switch"],
                       default_dict["vm2_freezestring"],
                       default_dict["vm2_method"],
                       default_dict["vm2_method_missing"],
                       default_dict["vm2_method_with_block"],
                       default_dict["vm2_module_ann_const_set"],
                       default_dict["vm2_module_const_set"],
                       default_dict["vm2_mutex"],
                       default_dict["vm2_newlambda"],
                       default_dict["vm2_poly_method"],
                       default_dict["vm2_poly_method_ov"],
                       default_dict["vm2_poly_singleton"],
                       default_dict["vm2_proc"],
                       default_dict["vm2_raise1"],
                       default_dict["vm2_raise2"],
                       default_dict["vm2_regexp"],
                       default_dict["vm2_send"],
                       default_dict["vm2_string_literal"],
                       default_dict["vm2_struct_big_aref_hi"],
                       default_dict["vm2_struct_big_aref_lo"],
                       default_dict["vm2_struct_big_aset"],
                       default_dict["vm2_struct_big_href_hi"],
                       default_dict["vm2_struct_big_href_lo"],
                       default_dict["vm2_struct_big_hset"],
                       default_dict["vm2_struct_small_aref"],
                       default_dict["vm2_struct_small_aset"],
                       default_dict["vm2_struct_small_href"],
                       default_dict["vm2_struct_small_hset"],
                       default_dict["vm2_super"],
                       default_dict["vm2_unif1"],
                       default_dict["vm2_zsuper"],
                       default_dict["vm3_backtrace"],
                       default_dict["vm3_clearmethodcache"],
                       default_dict["vm3_gc"],
                       default_dict["vm3_gc_old_full"],
                       default_dict["vm3_gc_old_immediate"],
                       default_dict["vm3_gc_old_lazy"],
                       default_dict["vm_symbol_block_pass"],
                       default_dict["vm_thread_alive_check1"],
                       default_dict["vm_thread_close"],
                       default_dict["vm_thread_condvar1"],
                       default_dict["vm_thread_condvar2"],
                       default_dict["vm_thread_create_join"],
                       default_dict["vm_thread_mutex1"],
                       default_dict["vm_thread_mutex2"],
                       default_dict["vm_thread_mutex3"],
                       default_dict["vm_thread_pass"],
                       default_dict["vm_thread_pass_flood"],
                       default_dict["vm_thread_pipe"],
                       default_dict["vm_thread_queue"],
                       default_dict["vm_thread_sized_queue"],
                       default_dict["vm_thread_sized_queue2"],
                       default_dict["vm_thread_sized_queue3"],
                       default_dict["vm_thread_sized_queue4"]
                       ]

    clear_col = pd.Series(clear_ruby_list)

    data_frame_test = {"Performance %d" % (loop_count + 1): test_col, "Default docker": default_col,
                       "clear docker": clear_col}

    df_exce_test = pd.DataFrame(data_frame_test)

    df_exce_test.to_excel(writer, sheet_name="ruby", index=False, startrow=9, startcol=4 * loop_count)

    print("Round %d Save Successfully Ruby!!!" % (loop_count + int(1)))


if __name__ == '__main__':
    loop_count = 0
    status_json_filename = r"C:\Users\xinhuizx\python_Code\MQ_script\2019-06-10\json\status\1560175612.json"
    writer = pd.ExcelWriter(r"C:\Users\xinhuizx\python_Code\MQ_script\MQ_tset.xlsx")

    # read_status_log(status_json_filename)
    for root_dir, _, files in os.walk(r"C:\Users\xinhuizx\python_Code\MQ_script\2019-06-10\json\test"):
        for json_filename in files:
            full_file_name = os.path.join(root_dir, json_filename)
            df_json = pd.read_json(full_file_name)
            # df_json = pd.read_json(r"C:\Users\xinhuizx\python_Code\MQ_scr\data_LOG.json")
            # Ruby(writer, df_json, loop_count)
            loop_count += 1

    writer.save()
