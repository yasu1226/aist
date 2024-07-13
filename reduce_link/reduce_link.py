import xml.etree.ElementTree as ET
import re

def xml_read(path):
  tree = ET.parse(path)
  root = tree.getroot()
  return root


def record_xml(root,new_file_name):
  tree = ET.ElementTree(root)
  tree.write(new_file_name, encoding="utf-8", xml_declaration=True)


def tag_insert(tag_name,append_name):
  new_tag = ET.Element("tag")
  new_tag.text = tag_name
  append_name.append(new_tag)


def add_degree_tag(exp_dir):
  root = xml_read(exp_dir)
  for node in root.findall(".//Node"):
    # Node内のlink要素の数をカウント
    link_count = len(node.findall("link"))
    # degreeタグを作成
    tag_insert(f"degree={link_count}",node)
  # XMLファイルとしてexp_dirに保存
  record_xml(root,"y_map.xml")
  
  
def degree1(target_id,count, root):
  for link in root.findall(".//Link"):
    link_id = link.get("id")
    if link_id == target_id:
      tag_count = 0
      for tag in link.findall("tag"):
        if tag.text is not None and tag.text[:2] == "_y":
          tag_count += 1
      if tag_count == 0:
        tag_insert(f"_y{str(count).zfill(3)}",link)
        count += 1
        break
  return count, root
  
def degree2_all_False(target_id,count,root):
  for link in root.findall(".//Link"):
    link_id = link.get("id")
    if link_id == target_id:
      tag_insert(f"_y{str(count).zfill(3)}",link)
      break
  return count, root

def search_added_tag(target_id,root):
  tag_found = False
  for link in root.findall(".//Link"):
      link_id = link.get("id")   
      if link_id == target_id:
        for tag in link.findall("tag"):
          if tag.text is not None and tag.text[:2] == "_y":
            tag_found = tag.text
            break
  return root, tag_found


def degree2_1_or_less_False(target_id, count, root, already_exist_y_id):
  for link in root.findall(".//Link"):
    link_id = link.get("id")
    if link_id == target_id:
      tag_count = 0
      for tag in link.findall("tag"):
        if tag.text is not None and tag.text[:2] == "_y":
          tag_count += 1
          if tag.text != already_exist_y_id:
            waste_text = tag.text
            link.remove(tag)
            root = delete_unnecessary_tag_and_add_another_tag(waste_text, root, link, already_exist_y_id)
            tag_insert(already_exist_y_id, link)
      if tag_count == 0:
        tag_insert(already_exist_y_id, link) 
  return count, root


def delete_unnecessary_tag_and_add_another_tag(waste_text, root, link, already_exist_y_id):
  for link in root.findall(".//Link"):
    for tag in link.findall("tag"):
      if tag.text is not None and tag.text == waste_text:
        link.remove(tag)
        tag_insert(already_exist_y_id, link)
  return root


# 重複して作成してしまったtagを1つに統合
def merge_duplicate_tags(root):
    for link in root.findall(".//Link"):
        unique_tags = set()  # 重複を排除するためのセットを作成する
        for tag in link.findall("tag"):
            # タグのテキストを取得してセットに追加する
            tag_text = tag.text
            if tag_text is not None:
                unique_tags.add(tag_text)
        # すべてのタグを削除する
        for tag in link.findall("tag"):
            link.remove(tag)
        # 重複を排除したタグをリンクに追加する
        for unique_tag in unique_tags:
            new_tag = ET.Element("tag")
            new_tag.text = unique_tag
            link.append(new_tag)
    return root  


def identify_degree(exp_dir):
  root = xml_read(exp_dir)
  count = 0
  for node in root.findall(".//Node"):
    for tag_element in node.findall("tag"):
      
      if tag_element.text == "degree=1":
        for link in node.findall("link"):
          # link_idを取得
          target_id = link.get("id")
          count, root = degree1(target_id, count, root)
          break

      if tag_element.text == "degree=2":
        target_ids = []
        for link in node.findall("link"):
          # link_idを取得
          target_id = link.get("id")
          target_ids.append(target_id)
        len_target_ids = len(target_ids)  
        # select_new_tag_numの中をすべてFalseで初期化
        select_new_tag_num = []
        select_new_tag_num = [False] * len_target_ids
        for num in range(len_target_ids):
          root, select_new_tag_num[num] = search_added_tag(target_ids[num], root)
        # もし新たに追加したtag("_yが含まれるもの)が、探索したすべてのLink(ここでは2つ)で見つからない場合
        if all(select_new_tag_num) == False:
          for num in range(len_target_ids):
            count, root = degree2_all_False(target_ids[num], count, root)
          count += 1
        # もし新たに追加したtag("_yが含まれるもの)が、探索したすべてのLink(ここでは2つ)の中で1つ見つかった場合
        if select_new_tag_num.count(False) == 1:
          for num in range(len_target_ids):
            if select_new_tag_num[num] != False:
              already_exist_y_id = select_new_tag_num[num]
          for link in node.findall("link"):
            # link_idを取得
            target_id = link.get("id") 
            count, root = degree2_1_or_less_False(target_id, count, root, already_exist_y_id)
        if select_new_tag_num.count(False) == 0:
          # どちらか一方のidを使用する(ここでは、先に取得したほうとする)
          already_exist_y_id = select_new_tag_num[0]
          for link in node.findall("link"):
            # link_idを取得
            target_id = link.get("id") 
            count, root = degree2_1_or_less_False(target_id, count, root, already_exist_y_id) 

      if tag_element.text == "degree=3" or tag_element.text == "degree=4" or tag_element.text == "degree=5":
        target_ids = []
        for link in node.findall("link"):
          target_id = link.get("id")
          target_ids.append(target_id)
        len_target_ids = len(target_ids) 

        select_new_tag_num = []
        select_new_tag_num = [False] * len_target_ids

        for num in range(len_target_ids):
          root, select_new_tag_num[num] = search_added_tag(target_ids[num], root)
          if select_new_tag_num[num] == False:
            for link in root.findall(".//Link"):
              link_id = link.get("id")   
              if link_id == target_ids[num]:
                tag_insert(f"_y{str(count).zfill(3)}",link)
                count += 1


  merge_duplicate_tags(root)
  record_xml(root,"yy_map.xml")
  record_xml(root,"/home/otsubo/CrowdWalk/crowdwalk/sample/tokyo/map/yy_map.xml")
  
  
def print_y(exp_dir):
  # パターン
  pattern = re.compile(r'_y\d{3}')
  # ファイルを開いてパターンにマッチする文字列を抽出
  with open(exp_dir, 'r') as file:
      data = file.read()
      all_y_items = pattern.findall(data)
  # 異なる要素の種類を抽出し、その数を取得する
  num_unique_items = len(set(all_y_items))
  # 結果を表示する
  print("要素の種類の数:", num_unique_items)


if __name__ == "__main__":
    # 実験ディレクトリ
    
    exp_dir = "map_new.xml"
    add_degree_tag(exp_dir)

    exp_dir = "y_map.xml"
    identify_degree(exp_dir)
    exp_dir = "yy_map.xml"
    print_y(exp_dir)
