"use client";
import { useState, useCallback } from "react";
import axios from "axios";
import { useDropzone } from "react-dropzone";
import { Card, CardHeader, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function Home() {
  const [file, setFile] = useState<File | null>(null);
  const [preview, setPreview] = useState<String | undefined | null>(null);
  const [score, setScore] = useState<Number | null>(null);
  const [loading, setLoading] = useState<Boolean>(false);

  // ✅ Handle dropped or selected files
  const onDrop = useCallback((acceptedFiles: File[]) => {
    const selectedFile = acceptedFiles[0];
    if (!selectedFile) return;
    setFile(selectedFile);
    setPreview(URL.createObjectURL(selectedFile));
    setScore(null); // reset score on new file
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: { "image/*": [] },
    maxFiles: 1,
  });

  const handleUpload = async () => {
    if (!file) {
      alert("Please select or drop an image first!");
      return;
    }

    try {
      setLoading(true);
      const formData = new FormData();
      formData.append("file", file);

      const res = await axios.post(
        process.env.NEXT_PUBLIC_BACKEND_URL + "/predict/",
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );

      setScore(res.data.score);
    } catch (err) {
      console.error(err);
      alert("Error analyzing image!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-indigo-100 via-white to-purple-100 p-4">
      <Card className="w-full max-w-lg">
        <CardHeader
          title="🎨 Image Aesthetic Scorer"
          subtitle="Drag & drop or click to upload an image"
        />
        <CardContent>
          <div
            {...getRootProps()}
            className={`border-2 border-dashed rounded-xl p-6 flex flex-col items-center justify-center cursor-pointer transition-colors ${
              isDragActive ? "border-indigo-500 bg-indigo-50" : "border-gray-300"
            }`}
          >
            <input {...getInputProps()} />
            {isDragActive ? (
              <p className="text-indigo-600 font-medium">Drop the image here...</p>
            ) : (
              <p className="text-gray-600 text-center">
                Drag & drop an image here, or click to select
              </p>
            )}
          </div>

          {preview && (
            <div className="mt-4 flex justify-center">
              <img
                src={preview as string}
                alt="preview"
                className="rounded-xl shadow-md max-h-64"
              />
            </div>
          )}

          <div className="mt-4 flex justify-center">
            <Button onClick={handleUpload} disabled={loading as boolean }>
              {loading ? "Analyzing..." : "Upload & Analyze"}
            </Button>
          </div>

          {score && (
            <p className="mt-4 text-lg font-medium text-gray-700 text-center">
              💎 Aesthetic Score:{" "}
              <span className="font-bold text-indigo-700">{score as number}/10</span>
            </p>
          )}
        </CardContent>
      </Card>
    </div>
  );
}
