table_list = [
    [ # header
        ["Component"], 
        ["Implemented"], 
        ["To be implemented (priority [1]_)"]
    ],

    [ # row1
        # column1
        ["File API"],

        # column2
        [
            "ncmpi_strerror",
            "ncmpi_strerrno",
            "ncmpi_create",
            "ncmpi_open/close",
            "ncmpi_enddef/redef",
            "ncmpi_sync",
            "ncmpi_begin/end_indep_data",
            "ncmpi_inq_path",
            "ncmpi_inq",
            "ncmpi_wait",
            "ncmpi_wait_all"
        ],

        # column3
        [
            "ncmpi_inq_libvers (3)",
            "ncmpi_set_fill (3)",
            "ncmpi_set_default_format (3)",
            "ncmpi_inq_put/get_size (3)",
            "ncmpi_delete (2)",
            "ncmpi_sync_numrecs (2)",
            "ncmpi_inq_file_info (3)",
            "ncmpi_inq_files_opened (3)",
        ],
    ],

    [ # row2
        # column1
        ["Dimension API"],

        # column2
        [
            "ncmpi_def_dim",
            "ncmpi_inq_ndims",
            "ncmpi_inq_dimlen",
            "ncmpi_inq_dim",
            "ncmpi_inq_dimname",
        ],

        # column3
        [],
    ],

    [ # row3
        # column1
        ["Attribute API"],

        # column2
        [
            "ncmpi_put/get_att_text",
            "ncmpi_put/get_att",
            "ncmpi_inq_att",
            "ncmpi_inq_natts",
            "ncmpi_inq_attname",
            "ncmpi_rename_att",
            "ncmpi_del_att",
        ],

        # column3
        [],
    ],

    [ # row4
        # column1
        ["Variable  API"],

        # column2
        [
            "ncmpi_def_var",
            "ncmpi_def_var_fill",
            "ncmpi_inq_varndims",
            "ncmpi_inq_varname",
            "ncmpi_put/get_vara",
            "ncmpi_put/get_vars",
            "ncmpi_put/get_var1",
            "ncmpi_put/get_var",
            "ncmpi_put/get_varn",
            "ncmpi_put/get_varm",
            "ncmpi_put/get_vara_all",
            "ncmpi_put/get_vars_all",
            "ncmpi_put/get_var1_all",
            "ncmpi_put/get_var_all",
            "ncmpi_put/get_varn_all",
            "ncmpi_put/get_varm_all",
            "ncmpi_iput/iget_var",
            "ncmpi_iput/iget_vara",            
        ],

        # column3
        [
            "ncmpi_iput/iget_var1 (1)",
            "ncmpi_iput/iget_vars (1)",
            "ncmpi_iput/iget_varm (1)",
            "ncmpi_iput/iget_varn (2)",
            "ncmpi_bput/bget_var (1)",
            "ncmpi_bput/bget_var1 (1)",
            "ncmpi_bput/bget_vara (1)",
            "ncmpi_bput/bget_vars (1)",
            "ncmpi_bput/bget_varm (1)",
            "ncmpi_bput/bget_varn (2)",
            "ncmpi_wait/wait_all (1)",
            "ncmpi_inq_nreqs (1)",
            "ncmpi_inq_buffer_usage/size (1)",
            "ncmpi_cancel (1)",
            "ncmpi_fill_var_rec (2)",
        ],
    ],
]
    
