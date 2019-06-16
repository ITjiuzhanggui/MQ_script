import json
import re
from pprint import pprint

data = {
    "default":
        {
            "httpd": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "golang": {},
            "node": {}, "openjdk": {}, "ruby": {}, "tensorflow": {}, "perl": {}
        },

    "clear":
        {
            "httpd": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {}, "golang": {},
            "node": {}, "openjdk": {}, "ruby": {}, "tensorflow": {}, "perl": {}
        },

    "status_def":
        {
            "httpd": {}, "golang": {}, "nginx": {}, "memcached": {}, "redis": {}, "php": {}, "python": {},
            "node": {}, "openjdk": {}, "ruby": {}, "tensorflow": {}, "perl": {}
        },

    "status_Clr":
        {
            "clearlinux_version": {}, "httpd": {}, "golang": {}, "nginx": {}, "memcached": {}, "redis": {},
            "php": {}, "python": {}, "node": {}, "openjdk": {}, "ruby": {}, "tensorflow": {}, "perl": {}
        }
}


def read_logs(file_name):
    with open(file_name, 'r', encoding="utf-8") as f:
        return f.readlines()


def DefRuby(lines):
    influs_list = ["app_answer", "app_answer", "app_erb", "app_factorial",
                   "app_fib", "app_lc_fizzbuzz", "app_mandelbrot", "app_pentomino",
                   "app_raise", "app_strconcat", "app_tak", "app_tarai", "app_uri",
                   "array_sample_100k_10", "array_sample_100k_11", "array_sample_100k__100",
                   "array_sample_100k__1k", "array_sample_100k__6k", "array_sample_100k___10k",
                   "array_sample_100k___50k", "array_shift", "array_small_and", "array_small_diff",
                   "array_small_or", "array_sort_block", "array_sort_float", "array_values_at_int",
                   "array_values_at_range", "bighash", "complex_float_add", "complex_float_div",
                   "complex_float_mul", "complex_float_new", "complex_float_power", "complex_float_sub",
                   "dir_empty_p", "enum_lazy_grep_v_100", "enum_lazy_grep_v_20", "enum_lazy_grep_v_50",
                   "enum_lazy_uniq_100", "enum_lazy_uniq_20", "enum_lazy_uniq_50", "erb_render",
                   "fiber_chain", "file_chmod", "file_rename", "hash_aref_dsym", "hash_aref_dsym_long",
                   "hash_aref_fix", "hash_aref_flo", "hash_aref_miss", "hash_aref_str", "hash_aref_sym",
                   "hash_aref_sym_long", "hash_flatten", "hash_ident_flo", "hash_ident_num", "hash_ident_obj",
                   "hash_ident_str", "hash_ident_sym", "hash_keys", "hash_literal_small2", "hash_literal_small4",
                   "hash_literal_small8", "hash_long", "hash_shift", "hash_shift_u16", "hash_shift_u24",
                   "hash_shift_u32", "hash_small2", "hash_small4", "hash_small8", "hash_to_proc",
                   "hash_values", "int_quo", "io_copy_stream_write", "io_copy_stream_write_socket",
                   "io_file_create", "io_file_read", "io_file_write", "io_nonblock_noex", "io_nonblock_noex2",
                   "io_pipe_rw", "io_select", "io_select2", "io_select3", "loop_for", "loop_generator",
                   "loop_times", "loop_whileloop", "loop_whileloop2", "marshal_dump_flo", "marshal_dump_load_geniv",
                   "marshal_dump_load_time", "require", "require_thread", "securerandom", "so_ackermann",
                   "so_array", "so_binary_trees", "so_concatenate", "so_count_words", "so_exception", "so_fannkuch",
                   "so_fasta", "so_k_nucleotidepreparing", "so_lists", "so_mandelbrot", "so_matrix",
                   "so_meteor_contest",
                   "so_nbody", "so_nested_loop", "so_nsieve", "so_nsieve_bits", "so_object", "so_partial_sums",
                   "so_pidigits", "so_random", "so_reverse_complementpreparing", "so_sieve", "so_spectralnorm",
                   "string_index", "string_scan_re", "string_scan_str", "time_subsec", "vm1_attr_ivar",
                   "vm1_attr_ivar_set",
                   "vm1_block", "vm1_blockparam", "vm1_blockparam_call", "vm1_blockparam_pass", "vm1_blockparam_yield",
                   "vm1_const", "vm1_ensure", "vm1_float_simple", "vm1_gc_short_lived",
                   "vm1_gc_short_with_complex_long",
                   "vm1_gc_short_with_long", "vm1_gc_short_with_symbol", "vm1_gc_wb_ary", "vm1_gc_wb_ary_promoted",
                   "vm1_gc_wb_obj", "vm1_gc_wb_obj_promoted", "vm1_ivar", "vm1_ivar_set", "vm1_length", "vm1_lvar_init",
                   "vm1_lvar_set", "vm1_neq", "vm1_not", "vm1_rescue", "vm1_simplereturn", "vm1_swap", "vm1_yield",
                   "vm2_array", "vm2_bigarray", "vm2_bighash", "vm2_case", "vm2_case_lit", "vm2_defined_method",
                   "vm2_dstr", "vm2_eval", "vm2_fiber_switch", "vm2_freezestring", "vm2_method", "vm2_method_missing",
                   "vm2_method_with_block", "vm2_module_ann_const_set", "vm2_module_const_set", "vm2_mutex",
                   "vm2_newlambda",
                   "vm2_poly_method", "vm2_poly_method_ov", "vm2_poly_singleton", "vm2_proc", "vm2_raise1",
                   "vm2_raise2",
                   "vm2_regexp", "vm2_send", "vm2_string_literal", "vm2_struct_big_aref_hi", "vm2_struct_big_aref_lo",
                   "vm2_struct_big_aset", "vm2_struct_big_href_hi", "vm2_struct_big_href_lo", "vm2_struct_big_hset",
                   "vm2_struct_small_aref", "vm2_struct_small_aset", "vm2_struct_small_href", "vm2_struct_small_hset",
                   "vm2_super", "vm2_unif1", "vm2_zsuper", "vm3_backtrace", "vm3_clearmethodcache", "vm3_gc",
                   "vm3_gc_old_full",
                   "vm3_gc_old_immediate", "vm3_gc_old_lazy", "vm_symbol_block_pass", "vm_thread_alive_check1",
                   "vm_thread_close",
                   "vm_thread_condvar1", "vm_thread_condvar2", "vm_thread_create_join", "vm_thread_mutex1",
                   "vm_thread_mutex2",
                   "vm_thread_mutex3", "vm_thread_pass", "vm_thread_pass_flood", "vm_thread_pipe", "vm_thread_queue",
                   "vm_thread_sized_queue", "vm_thread_sized_queue2", "vm_thread_sized_queue3", "vm_thread_sized_queue4"

                   ]
    data_ruby = {}
    for i in lines[
             # lines.index("[ruby] [INFO] Test clear docker image:\n"):
             lines.index("ruby/ruby.sh\n"):
             lines.index("Default-Ruby-Server\n")]:

        for startwith_item in influs_list:
            # if i.startswith(startwith_item) or i.startswith("\t") and startwith_item in i:
            if i.endswith("s/i)\n") and startwith_item in i:
                num = re.findall("\d+\.?\d*s", i)
                print(num)
                data_ruby.update({startwith_item: num[-1][:-1]})

        if "so_reverse_complementpreparing" in i:
            start = lines.index(i)
            so_reverse_complementpreparing = lines[start + 1]
            num = re.findall("\d+\.?\d*s", so_reverse_complementpreparing)
            data_ruby.update({"so_reverse_complementpreparing": num[-1][:-1]})

        if "so_k_nucleotidepreparing" in i:
            start = lines.index(i)
            so_reverse_complementpreparing = lines[start + 1]
            num = re.findall("\d+\.?\d*s", so_reverse_complementpreparing)

            data_ruby.update({"so_k_nucleotidepreparing": num[-1][:-1]})

    data.get("default").get("ruby").update(data_ruby)


if __name__ == '__main__':
    file_name = 'ruby.log'
    test = read_logs(file_name)
    DefRuby(test)
    pprint(data)
