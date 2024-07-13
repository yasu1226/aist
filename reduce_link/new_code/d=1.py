import xml.etree.ElementTree as ET
import random
import json

def xml_read(path):

  tree = ET.parse(path)
  root = tree.getroot()
  return root

def json_read(path):
    with open(path, "r") as f:
        results = json.load(f)
    return results

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
  
  
def degree1(exp_dir,target_id,count, root):

  for link in root.findall(".//Link"):

  #   # Node内のlink要素をすべて見ていく
  #   for link in node.findall("link"):

  #     # link_idを取得
  #     link = link.get("id")

  # idが一致するLinkを探索
    
    link_id = link.get('id')
    if link_id == target_id:
    
        
      print(link_id)
      # 新たにタグを追加
      # new_tag = ET.Element("tag")
      # new_tag.text = f"_y{count}\n"
      
      # link.append(new_tag)


      tag_insert(f"_y{str(count).zfill(3)}",link)
      record_xml(root,"yy_map.xml")
      count += 1
      break


  
  return count, root
  



def identify_degree(exp_dir):
  root = xml_read(exp_dir)
  count = 0
  for node in root.findall(".//Node"):
      
    for tag_element in node.findall("tag"):
          if tag_element.text == "degree=1":
              for link in node.findall("link"):

                # link_idを取得
                target_id = link.get("id")
              
                count, root = degree1(exp_dir,target_id,count, root)
                
                print(f"11111111{target_id}")
                print(count)

                break

          # if tag_element.text == "degree=2":
          #     print("2")
          
          # if tag_element.text == "degree=3":
          #     print("3")

  
  
  
  




if __name__ == "__main__":
    # 実験ディレクトリ
    
    exp_dir = "map_new.xml"
    add_degree_tag(exp_dir)


    exp_dir = "y_map.xml"
    identify_degree(exp_dir)
    