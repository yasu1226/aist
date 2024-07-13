def procedure(me, refs)
    increments_options = [0, 1, 2, 3]  # incrementsの候補
    total_area_limit = 818  # 増加面積の合計の制限

    # 1000回の並列シミュレーションを実行
    (0..1000).each do |num|
        run = me.createExecutableRun("tokyo_station", "ryzen1")
        
        # 各パラメータについてincrementsを決定し、増加面積を計算
        total_area = 0
        me.v[:dict_variable].each do |key, value|
            # incrementsをランダムに選択
            random_increments = increments_options.sample
            run.p[key]["increments"] = random_increments
            
            # 増加面積を計算して合計に加算
            length = value["length"].to_f
            area = length * random_increments
            total_area += area
        end
        
        # 増加面積の合計が制限を超える場合はincrementsを再設定
        if total_area > total_area_limit
            # 増加面積が制限以下になるまで再設定
            while total_area > total_area_limit
                me.v[:dict_variable].each do |key, value|
                    # incrementsをランダムに選択
                    random_increments = increments_options.sample
                    run.p[key]["increments"] = random_increments
                    
                    # 増加面積を再計算
                    length = value["length"].to_f
                    area = length * random_increments
                    total_area = 0
                    me.v[:dict_variable].each do |k, v|
                        total_area += v["length"].to_f * run.p[k]["increments"]
                    end
                end
            end
        end
    end
end